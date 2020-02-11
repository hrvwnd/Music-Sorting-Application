# project_music_sort-
The first project I undertook as part of my training with QA Consulting. 

## Brief

To create an individual project encorperating dev ops principles, using python to, encapsulating  git, basic linux, python web developement, continuous integration, the cloud and databases. 

## Solution

My project is to create an application that sorts music based on genre into seperate folders. This requires the program to read the id3 tags and find the artist information to compare with artists stored in a database under certain genres. 
The database consists of 3 tables: Artists, Genre and Tracks

## entity relation diagram 

Entity relationship diragram containing 3 tables. Related with 1/many to 1/many for for Artist <-> Genre  and 1 to 0/many for Genres <-> Tracks
![erd](https://i.imgur.com/b1n9yYU.png)

## Final Trello 

A trello board was used to keep track of the progress of the application

Unfortunately not all the user stories/ aims were met to provide total functionality.

![trello](https://i.imgur.com/WyfAkdi.png)

## Use Case Scenario

A diagram to show the processes the app should go through from a user and backend/ database perspective 

![UCS](https://i.imgur.com/ywFRDHf.jpg)

## Risk Assessment 

Assessment of risks involved in making the application 

![RA](https://i.imgur.com/VtXl95d.png)

## CI Pipeline 

The backend was written in python3 with modules: Flask (web dev framework), SQLAlchemy (Database query), Jinja2 (HTML with python). Using Trello for project management. Jenkins for automation and testing as well as deploying the flask application through gunicorn as a web server gateway interface. 

![CIP](https://i.imgur.com/WeTSift.png)
