from Importer.celery import app
from .models import Products
from django.contrib import messages
import csv, io, random

@app.task
def createProds(data_set):
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=','):
        if (random.randint(1,25) % 2 == 0):
            prodAct = True
        else:
            prodAct = False
        _, created = Products.objects.update_or_create(
            productSKU = column[1],

            defaults={
            'productName' : column[0],
            'productSKU' : column[1],
            'productDesc' : column[2],
            'productActive' : prodAct
            }
        )
        

