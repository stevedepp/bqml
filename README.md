# bqml
a GCP BQ ML model to be deployed on GAE

(please click on the demo video below to hear sound.).  
![demo](https://user-images.githubusercontent.com/38410965/111926054-a3e46280-8a81-11eb-89b1-db78ce24ffe6.mp4)

transcript:  
- **slide 0:**  hello everyone thank you for watching this video that quickly demos using local terminal and git for app development and Google app engine for production.  and finally a trigger linkage between them for CICD.  we start with the basics: app, main, requirements, and make file.    
- **slide 1:** import dependencies.  
- **slide 2:** test locally on a development server.  here we call **app create** before calling main.py with python but this could have gone in any order since app create still is a local development environment command.   
- **slide 3:** we improve the code locally and re test.  we can see logs change here in light blue as we hit the end point.     
- **slide 4:** deploy to production and hit the production server at Google.  
- **slide 5:** future development changes would be pushed to a development branch and then merged with master.  in this example any push from local terminal to GitHub master triggers a google app redeployment which is ...   
- **slide 7:** ... true cicd.  this is an example of that occurring, but ...   
- **slide 8:** ... there was and still is a wrinkle with permissions.  thank you for watching.
