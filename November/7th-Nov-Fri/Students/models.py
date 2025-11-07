from django.db import models


class Student(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Task(models.Model):
    task_name=models.CharField(max_length=100)
    describe=models.TextField()

class RankSheet(models.Model):
    tamil=models.IntegerField()
    english=models.IntegerField()
    maths=models.IntegerField()
    science=models.IntegerField()
    social=models.IntegerField()
    total=models.IntegerField()
    average=models.FloatField()
    result=models.BooleanField()