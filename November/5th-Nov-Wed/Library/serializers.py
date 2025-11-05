from rest_framework.serializers import ModelSerializer
from .models import *

class LaptopSerializer(ModelSerializer):
    
    class Meta:
        models=Laptop
        fields='__all__'