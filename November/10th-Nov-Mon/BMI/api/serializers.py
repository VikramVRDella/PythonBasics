from rest_framework.serializers import ModelSerializer
from .models import *

class BMI_Serializer(ModelSerializer):
    class Meta:
        model=BMICalculator
        fields='__all__'