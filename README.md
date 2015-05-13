# Online-FIR_Diary_lodging_System
Online FIR and Diary Lodging System

Development
===========

::Setup virtual environment::
-----------------------------

`virtualenv fir`

`source fir/bin/activate`

`pip install -r requirements.txt`

::Setting up database::
-----------------------

`./manage.py syncdb`

::Setting up SMS::
------------------

Since this is a demo project. I am using Free Site2SMS Api.
You need to register at mashape.com and Site2Sms Api.
Fill in your `uid`,`pwd` & `Mashape_Key` in `Web_App\Web_App\secret.py`

::Setting up Email::
--------------------

Since its a demo project, it currently uses my Gmail Account to send Emails.
For setting your Own email service you will need to set ,

`EMAIL_HOST`,`EMAIL_PORT`,`EMAIL_USE_TLS`,`EMAIL_HOST_PASSWORD`,`EMAIL_HOST_USER` fields in
`Web_App\Web_App\settings.py` file.

::RUN::
-------

`redis-server` //run redis server

`./manage.py runserver` //run application

To Do
=====

1. Use Django signals with websocket to update the Fir/GD on police portal.
2. Create an API.
3. Write Tests
4. Write a mobile Application.

For Further Query shoot me a mail at subho DOT prp AT gmail DOT com