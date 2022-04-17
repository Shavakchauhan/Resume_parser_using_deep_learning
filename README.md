# Resume_parser_using_deep_learning
Resume parser with ner using state of art in deep learning with transformers specifically [roberta](https://arxiv.org/abs/1907.11692).This project is a personal  project and not ready for production use but can decently perform parsing on the resumes and extract the keywords and match it with the best possible entitites which i have defined below.

The link for trained model is [link to model](https://www.dropbox.com/sh/22yw4b7jfk0edmp/AADsvQ9Gm9p0X0dsLgCQD8Z4a?dl=0)
.I did not added it on github because size was exceeding github size parameter.

There are seven types of entity possible for a given set of words:
1. Job title : This entity represents the the type of job which users wants
2. skill : This represents the importants skills which users possess
3. experience : This represents the job of the user in previous company and it timeline
4. org : This represents the set of companies ehich user has worked previously or working now.
5. tool : This represents the software tools used by user
6. Degree : This represents which degree user has taken for example B.Tech,M.tech,MBA etc
7. Educ : This represents the college in which user studied.


## Deployment
* Create virtual envinronment with python version==3.7.13
* Then download the generated_model folder(Link is given above) in Deployment folder
* Then in command line use pip3 install pip install -r requirements.txt
* Then run python3 main.py
* And on this  url [link](http://127.0.0.1:5000) you can upload your resume and then the model will give parsed output after sometime so that you will be able to see important keyword in the resume.

### Demo Gif of the Application
![Demo gif of the application](https://github.com/Shavakchauhan/Resume_parser_using_deep_learning/blob/main/demo_gif.gif)
