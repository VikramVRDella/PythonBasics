from rest_framework.serializers import ModelSerializer
from .models import *

class Student_Serializer(ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'

class Task_Serializer(ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'

class Student_Data_Serializer(ModelSerializer):
    all_task=Task_Serializer(many=True)
    class Meta:
        model=Student
        fields='__all__'

class Task_Data_Serializer(ModelSerializer):
    student_task= Student_Serializer()
    class Meta:
        model=Task
        fields='__all__'
