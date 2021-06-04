# System Architecture Diagram:
The below diagram shows the system architecture of web_app and rest api interface.
[![img1.png](https://i.postimg.cc/BQFRf5T6/img1.png)](https://postimg.cc/56xswCkd)

# Overview of the Web app:
This app is a Question-Answering application. The app has the below features:
1.	It can answer a question based on given context by the user. The input is question and context, and the output is answer.
2.	It can also process Bulk requests to answer the given set of questions. The users just need to upload an excel file with columns “question” and “context”. The app processes all the questions in the file and displays the answers on screen in tabular format.

link to web app: https://mgmt590-web-app-dk2fj6qmfq-uc.a.run.app/

# App Usage:
1.	The user can view all available models by clicking on the butten “Click to view available models”.
[![img2.png](https://i.postimg.cc/rw0skPh4/img2.png)](https://postimg.cc/fVsD7BQW)

2.	The user can add models in the “Add model” section by giving details such as model_name,tokenizer and model.
[![img3.png](https://i.postimg.cc/Dz1zWb3y/img3.png)](https://postimg.cc/94F2K0fv)

3.	The user can delete a model in the “Delete Model” section by selecting the model_name from the drop down list and then clicking “Delete Model” button.
[![img4.png](https://i.postimg.cc/dVb1tjXx/img4.png)](https://postimg.cc/gxKdg8GV)

4.	The user can provide question and context to the app in “Answer the question” section and get the answer on screen as shown below.
[![img5.png](https://i.postimg.cc/nzkc2bLy/img5.png)](https://postimg.cc/r0DkyHxj)

5.	The user can also upload an excel file in “Upload excel with questions and contexts” section containing the list of questions to be answered. The file should contain two columns “question” and “Context”. The app processes all the questions in the file and displays all answers in a tabular format.
[![img6.png](https://i.postimg.cc/nrhVwRjC/img6.png)](https://postimg.cc/2bgf1xxD)

# Dependencies:
The web app depends on the following
1.	Streamlit - https://streamlit.io/
2.	requests - https://pypi.org/project/requests/
3.	pandas - https://pandas.pydata.org/

# Building and running the web app locally via the Docker:
1.	A Docker file should be first created with all the dependencies and the requirements. This file contains info such as dependencies, relative target location of the code and other dependent files in target machine. Moreover, the file can also include the commands that should be executed when the docker is run.
[![img7.png](https://i.postimg.cc/ydB80Y7h/img7.png)](https://postimg.cc/06WvsvMr)

2.	Build the docker image using the below command.
docker build -t mgmt590 .
This creates the docker image mgmt590 in current working directory.
3.	Once the docker image is created, it can be executed using the super user(sudo) using below command.
Sudo docker run -it -p 8080:8080 mgmt590 /bash/ksh


