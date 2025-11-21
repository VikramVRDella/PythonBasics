from django.db import models

# Create your models here.
class AuthorModel(models.Model):
    name=models.CharField(max_length=100)

class BookModel(models.Model):
    title=models.CharField(max_length=100)
    author=models.ForeignKey(AuthorModel, on_delete=models.CASCADE,related_name='books')
    published_year=models.IntegerField(default=0)
