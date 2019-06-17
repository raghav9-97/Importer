# Product Importer

## Overview
This project helps in importing products from .csv file to PostgreSQL database and gives the option to search and filter these products in accordance with need.User can delete all the products at a single click of a button or individual deletion is also provided.

## Installation Guide
This project uses redis-server, Celery, PostgreSQL as a database backend.

### Use Python 3
Create virtual environment and install dependencies.
```
virtualenv env
source env/bin/activate
git clone https://github.com/raghav9-97/Importer.git
cd Importer
pip install -r requirements.txt
```

### Running Server
Follow the steps and commands in different terminals for starting the server.
```
redis-server
```
Navigate to the virtualenv directory.
```
source env/bin/activate
celery -A Importer worker -l info
```
Navigate to the Product Importer directory.
```
cd Importer
python manage.py runserver
```