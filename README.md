# TEXT SIMILARITY OVERVIEW
This solution is meant to take in as inputs two texts and uses a metric to determine how similar they are. Documents that are exactly the same should get a score of 1, and documents that don’t have any words in common should get a score of 0.

# Installation and Running Steps
This section of the document will walk you through installing and running the project.
First you should clone this repository and then navigate to the correct directory.

## 1. Python Environment
  This section of the document is unnecessary if you want run the Docker Container and don't want to use the testing capabilites of this repository.
  After navigating into the correct directory we must set up the python dependencies.  
  
  ### 1.1 Installing Python
  The first thing we need to do is ensure Python is installed on your machine. 
  To check if python is installed on your machine open up a terminal and run:
  
      python --version
  If a version is shown after running this command it means python is installed on your machine. Otherwise you should follow this tutorial to install python https://realpython.com/installing-python/

### 1.2 Installing Pip
Next we will want to ensure that pip is installed on your machine.
If you are unsure if pip is installed on you machine run 

    python -m pip --version
Just like above if a version is shown after this command it means you have pip installed otherwise follow this tutorial to install pip
https://pip.pypa.io/en/stable/installing/


### 1.3 Virtual Environment Setup
After installing pip we need to set up a virtual environment. 
In terminal on Mac or Linus run:

    pip install virtualenv
    python virtualenv venv
    source venv/bin/activate
    pip install -r requirements.txt

or in powershell for windows run:

    pip install virtualenv
    python -m virtualenv venv
    .\venv\Scripts\activate
    pip install -r requirements.txt

