from django.db import models

class BMICalculator(models.Model):
    weight=models.FloatField()
    height=models.FloatField()
    bmi=models.FloatField()
    category=models.CharField(max_length=100)
