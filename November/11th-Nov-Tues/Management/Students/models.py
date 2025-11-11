from django.db import models

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()



class Task(models.Model):
    student_task=models.ForeignKey(Student,related_name='all_task',null=True,on_delete=models.CASCADE)
    task_name=models.CharField(max_length=100)
    describe=models.TextField()


