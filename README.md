# heutagogy_server

This is the back-end server for heutagogy application.  
This is a Django REST Server, which provides api paths to
download/update lessons in the application.  
The default Django Admin is configured for easy adding of Lessons
and Tests for the same.
  
Steps to setup the server locally:
* Download the repo
  > `git clone https://github.com/piyush9311/ATL_Server.git`
 
* Setup virtual environment
  > `virtualenv venv --python=python3`

* Install dependencies
  > `source ./venv/bin/activate`
  > `pip3 install -r requirements.txt`

* Run the server
  > `python3 manage.py runserver 0.0.0.0:8000`
 
 
