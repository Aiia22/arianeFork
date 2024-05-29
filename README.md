#### STEPS SETUP

## Run command to create Django Project:

django-admin startproject arianefork

## Docker set up:

1-create dockerfile
2-create docker-compose.yml
3-run command to build and run containers: docker-compose up --build

## Got issues with Web container so I created requirements.txt

1-run command to auto-generate requirements.txt: pip freeze > requirements.txt
2-modified setup of dockerfile to have correct python version
3-rebuild Docker Image :

- remove containers: docker-compose down
- Build and up containers: docker-compose up --build

## Apply Database Migrations to resolve unapplied migrations mentioned in log

run command : docker-compose run web python manage.py migrate
Why ? ==> Execute migrations within Docker container, setting up database tables according to Django models.

## Create a Superuser for Django Admin

run command to create superuser: docker-compose run web python manage.py createsuperuser
Why? ==> To access Django admin panel, a user with superuser privileges is required.

## Access Django Application

Access Django App : http://localhost:8000
Access Django Admin panel: http://localhost:8000/admin

## Create Guest Book App

run command : docker-compose run web python manage.py startapp guestbook
Why? ==> Because I use docker for the project I execute the command via docker compose.

## Development App process

1- Define model
2- Create and apply the migrations to guestbook app:
-add guestbook as installed app in settings.py
-docker-compose run web python manage.py makemigrations guestbook
-docker-compose run web python manage.py migrate
3- Build the views
4- Create a Form for the model
5- Setup templates:
-create folder templates inside guestbook repo
-create the html file to display form and list entries
6- Configure URLs
7- Test application

## Monitor and Manage Containers

docker-compose up # Start the application
docker-compose down # Stop the application
docker-compose logs # View logs of all services
