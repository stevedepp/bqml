### A Google Cloud Platform BigQuery Machine Learning model deployed on Google App Engine

(please click on the demo video below to hear sound.).  
![demo](https://user-images.githubusercontent.com/38410965/111926054-a3e46280-8a81-11eb-89b1-db78ce24ffe6.mp4)

#

> Hello thank you for watching my video. Objective for this weeks project is to employ BQ ML to serve up an ML model
and deploy that to Google App Engine.  Via command line, I was able to coerce BQ ML to create and serve a model locally 
and present model evaluation in a shell script, but i wasn’t able to serve the evaluation not locally in a web browser.  I learned a lot of BQ and gcloud command line during this experience and found ways ... 

**Demo Video 5:**
### BQ ML served via Google App Engine.

**Steve Depp
MSDS 434 section 55** 

**Objectives: functions**   
- [x] BQ ML create a binary logistic regression model via CREATE MODEL
- [x] ML.EVALUATE to evaluate
- [ ] ML.PREDICT to serve predictions 

**Objectives: engineering**  
- [x] Local BQML model creation
- [x] Local serving of BQML model description
- [x] Terminal BQ ML model evaluation
- [ ] Local serving BQML model evaluation
- [ ] Google App Engine

**Hair pulls**  
- [x] Managing datasets dynamically
- [x] App Engine dynamics
- [x] Reinstalling gcloud 

**Learning**  
- [x] BQ command line
- [x] BQ Python SDK command line
- [x] Service accounts via command line
- [x] Make files

<img width="682" alt="Last login Sat 0 17 195923 on console" src="https://user-images.githubusercontent.com/38410965/113489226-fe71bb80-9490-11eb-95eb-aad3a75b2589.png">

#

> ... to make Makefiles very useful. For example, I set up this make file entry ...

### BQ ML served via Google App Engine.

Makefile
-	make setup
-	make install
-	make lint
-	make setup_bq
-	make run
-	make dev

—> setup
￼
<img width="1298" alt="bqml_dv make setup" src="https://user-images.githubusercontent.com/38410965/113489238-18ab9980-9491-11eb-8a8d-40d9622fae0e.png">

Makefile

—> install
￼
<img width="682" alt="stevedepp@Steves-MBP-2" src="https://user-images.githubusercontent.com/38410965/113489250-324ce100-9491-11eb-940b-f212b1eee65b.png">

#

> ... shown here at bottom to reestablish connects between service accounts and keys. [pause] When 'make run' ... 

Makefile

—> lint
￼
<img width="682" alt="imported as pi" src="https://user-images.githubusercontent.com/38410965/113489273-56102700-9491-11eb-8d6a-f315a60ad4ba.png">

Makefile

—> setup_bq
-	makes credentials dir / file
-	deletes / adds / binds
	-	service account
	-	keys
-	sets environment variable

<img width="682" alt="stevedepp@Steves-MBP-2  dv05bqml_dv" src="https://user-images.githubusercontent.com/38410965/113489265-498bce80-9491-11eb-92c4-b96c94e38069.png">

#

> ... runs the main.py file, the BQML model descriptors are served locally, and  those descriptors show up ... 

Makefile

—> run
	python3 run main.py
￼
<img width="703" alt="dataset alive already toss and make fresh" src="https://user-images.githubusercontent.com/38410965/113489478-83110980-9492-11eb-804d-3b6796f32eb6.png">

Local serving 

Model description on web browser
￼
<img width="745" alt="127 0 0 1" src="https://user-images.githubusercontent.com/38410965/113489482-886e5400-9492-11eb-8561-ab060b2ee7de.png">

#

> ... at GCP as well, as did ...

@GCP

Model description

<img width="686" alt="console cloud google com" src="https://user-images.githubusercontent.com/38410965/113489508-a76ce600-9492-11eb-98b0-050369205203.png">

#

> training indicators, and ...

@GCP

Model training

<img width="1011" alt="Google Cloud Platform" src="https://user-images.githubusercontent.com/38410965/113489517-b94e8900-9492-11eb-8fd1-a8e40de8e458.png">

#

> ... model evaluations. Model evaluations ...

@GCP

Model evaluation

<img width="1011" alt="Google Cloud Platform 8 msds-434-depp-dv5" src="https://user-images.githubusercontent.com/38410965/113489527-c9666880-9492-11eb-8f1b-c07aa0760a0c.png">

#

> ... worked fine in a shell script . [pause] Up here on top is BQML returning an evaluation of the logistic model, but local serving of evaluations to a browser didn’t go so well despite a million tries. (Thus, the usefulness of Make files!). Lastly, as I mentioned, I learned alot about dynamically controlling datasets via command line and ...

Local Serving

Model evaluation - shell
￼
Model evaluation - browser via Flask

<img width="745" alt="TypeError" src="https://user-images.githubusercontent.com/38410965/113489545-e26f1980-9492-11eb-83e3-cbaca2658809.png">

#

> ... via Flask [pause].  Here is a route to clean up datasets so that the model can be re run.  

Local serving 

Clean up

<img width="686" alt="ound one" src="https://user-images.githubusercontent.com/38410965/113489569-f61a8000-9492-11eb-8168-c2f2d3974e5c.png">

Restart

<img width="703" alt="make run" src="https://user-images.githubusercontent.com/38410965/113489571-f87cda00-9492-11eb-962e-57180886dc09.png">

#

> A quick review of code is provide here.  Here at bottom, I am showing you a "try except" routine for checking whether a data set needs to be created for the model to run.

BQ ML served via Google App Engine.

Code

Removing data sets dynamically

<img width="767" alt="from google cloud import bigquery" src="https://user-images.githubusercontent.com/38410965/113489591-14807b80-9493-11eb-9847-30fccb6ef198.png">

#

CREAT MODEL —> Model description 

<img width="712" alt="29 bigquery-public-data google_analytics_sample ga_sessions_+" src="https://user-images.githubusercontent.com/38410965/113489602-2cf09600-9493-11eb-98bb-256738992ca2.png">

#

Model evaluation 

<img width="719" alt="Ln 37, Col 13 Spaces 4 UTF-8 LE Python R" src="https://user-images.githubusercontent.com/38410965/113489620-3bd74880-9493-11eb-95eb-3406f7cf5866.png">

#

> And here’s the cleanup route in Flask to delete datasets.

Flask

<img width="786" alt="stevedepp  Documents" src="https://user-images.githubusercontent.com/38410965/113489630-4d205500-9493-11eb-90af-1c70438a351b.png">

#

> And, as I said deploying didnt go well, ...

BQ ML served via Google App Engine.

Deploy
https://msds-434-depp-dv5.ue.r.appspot.com

<img width="682" alt="stevedepp staff" src="https://user-images.githubusercontent.com/38410965/113489636-5f01f800-9493-11eb-85dc-9c5b32269120.png">

<img width="997" alt="502 Bad Gateway" src="https://user-images.githubusercontent.com/38410965/113489638-61fce880-9493-11eb-9a98-db870dea01c2.png">

#

> ... but that just leaves more fun to do ...


Deploy

<img width="682" alt="bqml_dv-stevedepp@Steves-MBP-2" src="https://user-images.githubusercontent.com/38410965/113489677-907ac380-9493-11eb-9df1-115af16cbecc.png">

#

> ... next week.

BQ ML served via Google App Engine.

Next steps
- [ ] Logs
- [ ] Tests
- [ ] Modular design
    - [ ] CREATE MODEL
    - [ ] EVALUATE MODEL
    - [ ] web.app 
- [ ] @click

#



