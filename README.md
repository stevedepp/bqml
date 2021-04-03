# bqml
a GCP BQ ML model to be deployed on GAE

(please click on the demo video below to hear sound.).  
![demo](https://user-images.githubusercontent.com/38410965/111926054-a3e46280-8a81-11eb-89b1-db78ce24ffe6.mp4)

#

Demo Video 5
BQ ML served via Google App Engine.

Steve Depp
MSDS 434 section 55 

Objectives: functions 
- [x] BQ ML create a binary logistic regression model via CREATE MODEL
- [x] ML.EVALUATE to evaluate
- [ ] ML.PREDICT to serve predictions 

Objectives: engineering
- [x] Local BQML model creation
- [x] Local serving of BQML model description
- [x] Terminal BQ ML model evaluation
- [ ] Local serving BQML model evaluation
- [ ] Google App Engine

Hair pulls
- [x] Managing datasets dynamically
- [x] App Engine dynamics
- [x] Reinstalling gcloud 

Learning
- [x] BQ command line
- [x] BQ Python SDK command line
- [x] Service accounts via command line
- [x] Make files

<img width="682" alt="Last login Sat 0 17 195923 on console" src="https://user-images.githubusercontent.com/38410965/113489226-fe71bb80-9490-11eb-95eb-aad3a75b2589.png">

#

BQ ML served via Google App Engine.

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



