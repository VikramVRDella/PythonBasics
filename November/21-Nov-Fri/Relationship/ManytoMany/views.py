from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class StudentView(ModelViewSet):
    queryset=StudentModel.objects.all()
    serializer_class=StudentSerializer

class CourseView(ModelViewSet):
    queryset=CourseModel.objects.all()
    serializer_class=CourseSerializer