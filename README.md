# TEXT SIMILARITY OVERVIEW
This solution is meant to take in as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

- [Installation and Running Steps](#installation-and-running-steps)
  * [1. Python Environment](#1-python-environment)
    + [1.1 Installing Python](#11-installing-python)
    + [1.2 Installing Pip](#12-installing-pip)
    + [1.3 Virtual Environment Setup](#13-virtual-environment-setup)
  * [2 Docker](#2-docker)
  * [3 Running the flask app without Docker](#3-running-the-flask-app-without-docker)
  * [4 Testing and Using the model](#4-testing-and-using-the-model)


# Installation and Running Steps
This section of the document will walk you through installing and running the project.
Before doing anything else, you should clone this repository and then navigate to the correct directory where this repository was cloned.

## 1. Python Environment
  This section of the document is unnecessary if you want to run the Docker Container and don't want to use the testing capabilities of this repository.
  After navigating into the correct directory we must set up the python dependencies.  
  
  ### 1.1 Installing Python
  The first thing we need to do is ensure Python is installed on your machine. 
  To check if python is installed on your machine open up a terminal and run:
  
      python --version
  If a version is shown after running this command it means python is installed on your machine. Otherwise, you should follow this tutorial to install python https://realpython.com/installing-python/

### 1.2 Installing Pip
Next, we will want to ensure that pip is installed and has been updated recently on your machine.
If you are unsure if pip is installed on your machine run 

    python -m pip --version
    pip install --upgrade pip
Just like above if a version is shown after this command it means you have pip installed. Otherwise, follow this tutorial to install pip
https://pip.pypa.io/en/stable/installing/

### 1.3 Virtual Environment Setup
After installing pip we need to set up a virtual environment. 
In a terminal on Mac or Linus run:

    pip install virtualenv
    python virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

or in powershell for windows run:

    pip install virtualenv
    python -m virtualenv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt

## 2 Docker
If you want to run this solution using docker, you first must have docker installed.
If you are unsure if you have docker installed here is more information on how to do so 
https://docs.docker.com/get-docker/

After installing Docker you can then return to the terminal.
In the terminal you should then run the command

    docker pull ndfinelli/text-similarity-flask-app

This command will pull the latest docker image.

To run this docker image you should run

    docker run -d -p 5000:5000 ndfinelli/text-similarity-flask-app

The sever should be running and if you navigate to http://0.0.0.0:5000/ you should see a web page with the text Text Similarity Comparision Server.
If this is the case you can head to [4 Testing and Using the model](#4-testing-and-using-the-model)

## 3 Running the flask app without Docker
If you don't have docker installed and don't want to go through the steps of installing it below are the steps needed to run the flask server without it.

To do any of the following steps you first must ensure that you have gone through all the steps in [Python Evironment](#1.-python-environment) of this document.

Once you have pip installed, have created a virtual environment, and have installed all the dependencies running the flask server is fairly easy.
All you need to do is run the command

    python -m server.main

This should start the flask server and you should see output similar to 

    Nico:text_similarity nicofinelli$ python -m server.main
    * Serving Flask app "main" (lazy loading)
    * Environment: production
      WARNING: This is a development server. Do not use it in a production deployment.
      Use a production WSGI server instead.
    * Debug mode: off
    * Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

 The model should be running and if you navigate to http://0.0.0.0:5000/ you should see a web page with the text Text Similarity Comparision Server

 ## 4 Testing and Using the model
After either using docker to serve the model or running the model manually we now need to test the model.

To test this model without installing Python and all of the dependencies you should post a request to 'http://localhost:5000/text_similarity_comparison' with the two texts you wish to compare in the body of the request in the format of {tests: [text1, text2]}

To utilize this repository's tests all you must do is enter the command

    python -m model.test_endpoint
    
After running this command you should see the the output comparing all the sample texts that were provided in data section of this repository.
