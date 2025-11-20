from rest_framework.serializers import ModelSerializer
from .models import *

class StduentSerializer(ModelSerializer):
    class Meta:
        model=StduentModel
        fields='__all__'