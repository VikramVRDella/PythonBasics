from django.db import models

class TodoModel(models.Model):
    task=models.CharField(max_length=100)
    describe=models.TextField()
    # is_completed=models.BooleanField()