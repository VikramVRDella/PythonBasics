from django.db import models

# Create your models here.
class CourseModel(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name

class StudentModel(models.Model):
    name=models.CharField(max_length=100)
    courses=models.ManyToManyField(CourseModel,related_name='students',null=True)

    def __str__(self):
        return self.name