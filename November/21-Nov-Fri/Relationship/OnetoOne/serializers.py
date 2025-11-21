from rest_framework.serializers import ModelSerializer
from .models import *


class ProfileSerializer(ModelSerializer):
    class Meta:
        model=ProfileModel
        fields='__all__'