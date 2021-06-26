# Quiz Game

A small quiz game application created with Django, Redis and Open Trivia Database API.

![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/main-page.png "Main Page Image")

## Features

- **Big Amount Of Questions.** Open Trivia Database API provides 4,050 verified questions.
- **Leaderboard.** Leaderboard, based on Redis, gives you ability to track your score on leaderboard.

## Installation

### 1. Install using Docker

1. Create a working directory called ```django_quiz``` and put files from repository in it.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/docker_1_1.jpg "Docker Install 1.1")
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/docker_1_2.jpg "Docker Install 1.2")

2. Place ```docker-compose.yml``` file from repository near working directory folder.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/docker_2.jpg "Docker Install 2")

3. Open terminal in a directory with working directory and ```docker-compose.yml``` file and run ```docker-compose build```.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/docker_3.jpg "Docker Install 3")

4. Run ```docker-compose up```.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/docker_4.jpg "Docker Install 4")

5. Open a new terminal window and find a docker container id using command ```docker ps```.
6. Run ```docker exec -it <container_id> python manage.py migrate``` to make migrations to database.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/docker_6_1.jpg "Docker Install 6.1")
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/docker_6_2.jpg "Docker Install 6.2")

7. Installation complete. Use ```127.0.0.1:8000``` address to access the website.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/docker_7.jpg "Docker Install 7")


### 2. Install using Virtualenv

***To make app work you should have running PostgreSQL and Redis servers on your machine.*** 

1. Create a working directory and put files from repository in it.
2. In directory with working directory run ```virtualenv venv```.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/venv_2.jpg "Virtualenv Install 2")

3. Run ```source virtualenv/bin/activate``` (Linux) or go to ```venv/Scripts``` directory and run ```activate``` (Windows)  to activate virtual environment.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/venv_3.jpg "Virtualenv Install 3")

4. Go to the working directory and run ```pip install -r requirements.txt```.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/venv_4.jpg "Virtualenv Install 4")

5. Run ```PostgreSQL``` and ```Redis``` servers.
6. Run ```python manage.py migrate``` to make migrations to database.
   
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/venv_6_1.jpg "Virtualenv Install 6.1")
![alt text](https://github.com/zalexvic/python-django-quiz/blob/develop/readme_images/venv_6_2.jpg "Virtualenv Install 6.2")

7. Installation complete. Run ```python manage.py runserver``` and use ```127.0.0.1:8000``` address to access the website.


## Resources
Question Mark Pic: [Link](https://www.pixilart.com/art/pixel-mario-question-mark-block-a16e719614a255f)
Riddler Pic: [Link](https://alcreed.tumblr.com/image/110508401819)
Open Trivia Database API: [Link](https://opentdb.com/api_config.php)