from django.db import models

# Create your models here.
class Persons(models.Model):
    name=models.CharField(max_length=150)
    age=models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    task_name=models.CharField(max_length=200)
    describe=models.TextField()

class RankModel(models.Model):
    tamil=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()
    social=models.IntegerField()
    total=models.IntegerField()
    average=models.FloatField()
    result=models.BooleanField()