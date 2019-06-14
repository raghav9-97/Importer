from django.db import models

class Products(models.Model):
    productName = models.CharField(max_length=2000)
    productSKU = models.CharField(primary_key=True,max_length=2000)
    productDesc = models.TextField()
    productActive = models.BooleanField()