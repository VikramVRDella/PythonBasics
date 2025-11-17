from django.db import models

# Create your models here.

class Book(models.Model):
    title=models.CharField(max_length=100)
    describe=models.TextField()

class Laptop(models.Model):
    brand=models.CharField(max_length=100)
    modelname=models.CharField(max_length=100)
    user_type=models.CharField(max_length=100,null=True)

