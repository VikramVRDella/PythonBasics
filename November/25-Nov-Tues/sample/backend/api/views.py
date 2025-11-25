from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class ViewModel(APIView):
    def get(self,request):
        fetch=StudentModel.objects.all()
        student=StudentSerializer(fetch,many=True).data
        return Response(student)

