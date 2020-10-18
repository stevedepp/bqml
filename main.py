from google.cloud import bigquery
import pandas as pd
from flask import Flask
from flask import jsonify

p = 'msds-434-depp-dv5'
d = 'demo_dataset'
m = 'demo_model'
loc = 'US'
model = f'{d}.{m}'
dataset_id = f'{p}.{d}'
dataset = bigquery.Dataset(dataset_id)
dataset.location = loc
client = bigquery.Client(project=p)

try:
    client.get_dataset('msds-434-depp-dv5.demo_dataset')
    print('dataset alive already: toss and make fresh')
    client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)
    dataset = client.create_dataset(dataset, timeout=30)
except:
    dataset = client.create_dataset(dataset, timeout=30)
    print('no dataset; make another')
    
job_config = bigquery.QueryJobConfig()

sql_model = f"""
#standardSQL
CREATE MODEL `{model}`
OPTIONS(model_type='logistic_reg') AS
SELECT
IF(totals.transactions IS NULL, 0, 1) AS label,
IFNULL(device.operatingSystem, "") AS os,
device.isMobile AS is_mobile,
IFNULL(geoNetwork.country, "") AS country,
IFNULL(totals.pageviews, 0) AS pageviews
FROM
`bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE
_TABLE_SUFFIX BETWEEN '20160801' AND '20170630'
"""

model_job = client.query(sql_model, job_config=job_config)

model_json = {'running':model_job.running(),
        'project':p,
        'dataset':d,
        'model':m,
        'dataset id':dataset_id
    }

def eval():
    sql_eval = f"""
    SELECT
        *
    FROM
        ML.EVALUATE(MODEL `{model}`, (
        SELECT
            IF(totals.transactions IS NULL, 0, 1) AS label,
            IFNULL(device.operatingSystem, "") AS os,
            device.isMobile AS is_mobile,
            IFNULL(geoNetwork.country, "") AS country,
            IFNULL(totals.pageviews, 0) AS pageviews
        FROM
            `bigquery-public-data.google_analytics_sample.ga_sessions_*`
        WHERE
            _TABLE_SUFFIX BETWEEN '20170701' AND '20170801'))"""
    eval_job = client.query(sql_eval, job_config=job_config)
    return eval_job

app = Flask(__name__)

@app.route('/')
def hello():
    """ return friendly HTTP greeting."""
    return f'Hello from BQ ML structure is{model_json}'

#@app.route('/model/')
#def model():
#    return model_job.running()

@app.route('/eval/')
def e():
    result = eval()
    df = result.to_dataframe()
    dict = df.to_dict
    return df

@app.route('/cleanup/')
def cleanup():
    try:
        client.delete_dataset(dataset_id, delete_contents=True, not_found_ok=True)
        return f'found one and killed it'
    except:
        return 'no dataset found'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
