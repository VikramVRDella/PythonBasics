from rest_framework.serializers import ModelSerializer
from .models import *

class StudentSerializer(ModelSerializer):
    class Meta:
        model=StudentModel
        fields='__all__'


class CourseSerializer(ModelSerializer):
    class Meta:
        model=CourseModel