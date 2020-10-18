install:
	pip3 install --upgrade pip
	pip3 install -r requirements.txt

dev:
	pip3 install ipython
	ipython

lint:
	pylint -disable-R,C main.py

setup:
	python3 -m venv .venv

setup_bq:
	mkdir -p ../.credentials
	touch ../.credentials/bqml-depp.json
	pip install --upgrade google-cloud-bigquery
	gcloud config set project msds-434-depp-dv5
	gcloud iam service-accounts delete bqml-depp@msds-434-depp-dv5.iam.gserviceaccount.com
	gcloud iam service-accounts create bqml-depp
	gcloud projects add-iam-policy-binding msds-434-depp-dv5 --member "serviceAccount:bqml-depp@msds-434-depp-dv5.iam.gserviceaccount.com" --role "roles/owner"
	gcloud iam service-accounts keys create ../.credentials/bqml-depp.json --iam-account bqml-depp@msds-434-depp-dv5.iam.gserviceaccount.com
	export GOOGLE_APPLICATION_CREDENTIALS='/Users/stevedepp/Documents/Personal/MSDS/434/week 05/dv05/.credentials/bqml-depp.json'

run:
	python3 main.py
