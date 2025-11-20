from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Avg,Min,Max

class Student(APIView):
    def get(self,request):
       get_student=StduentModel.objects.filter(name__in=["John"])
       serial=StduentSerializer(get_student,many=True).data
    #    serial=StduentSerializer(get_student).data
       return Response(serial)
    
    def post(self,request):
        Serial=StduentSerializer(data=request.data)
        if Serial.is_valid():
            Serial.save()
            return Response("New Student Created")
        else:
            return Response(Serial.errors)