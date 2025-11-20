from django.db import models

# Create your models here.
class StduentModel(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    joined_date=models.DateField(null=True,blank=True)

