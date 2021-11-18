# Database Duality REST API - Simple CRM
Django REST API project which enables dual databases (namely, PostgreSQL and MongoDB) with transaction support.

## Concept:
**Django framework** is a robust framework to build easy to go live RESTful APIs when used along with Django Rest Framework. But it lacks support for NoSQL databases like MongoDB when compared to SQL counter parts. 

There are ways to connect to MongoDB through various libraries namely - *pymongo*, *mongoengine* and *Djongo*. 

The most easy to use MongoDB library for Django is Djongo library, as it mirrors the Django ORM. The ORM is then converted to ODM and make database calls.

## Approach:
I wanted to explore each of the above mentioned libraries and see which one is the most suitable for my needs. 

- Please check the repo [pymongo-django-rest-api](https://github.com/muler-opensource/django-rest-api-pymongo-template) for the pymongo library. Please check both the branches. 
    - `main` branch contains basic pymongo usage
    - `pymongo-transactions` branch contains as the name suggests pymongo usage with transactions support
- I'm going to create a Django application to create a simple CRM application to mimic Salesforce
- There will be four apps in this application
    - Marketing Cloud
    - Sales Cloud
    - Service Cloud
    - User Management
- The apps will be connected to different databases.
- Since Marketing Cloud, Sales Cloud and Service Cloud are related to each other, I will come up with a design for this relationship.
- User Management app is connected to PostgreSQL database, as it will be easy since Django has its own Admin Portal, which I'm going to leverage for it.

## Design:
 > TO BE ADDED

## Intial Steps:
To use or run the django app, please use GnuMake / Make tool to run the following commands:
- `make run`: Creates the python virtual environment.Activates the Virtual Environment and installs all the required packages in requirements.txt file.
- `make requirements`: Updates the requirements.txt file.
- `make clean`: To remove the __pycache__, **.vscode**, **.idea** folders.