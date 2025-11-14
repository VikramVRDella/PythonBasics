from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class StudentAPI(APIView):
    def get(self,request,id=None):
        if id==None:
            all_students=StudentModel.objects.all()
            fetch=StudentSerializer(all_students,many=True).data
            return Response(fetch)
        else:
            one_student=StudentModel.objects.get(id=id)
            fet=StudentSerializer(one_student).data
            return Response(fet)
    
    def post(self,request):
        student=StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response("New Student Updated")
        else:
            return Response(student.errors)
    
    def put(self,request,id):
        fetch_student=StudentModel.objects.get(id=id)
        update_student=StudentSerializer(fetch_student,data=request.data,partial=True)
        if update_student.is_valid():
            update_student.save()
            return Response("Student Updated")
        else:
            return Response(update_student.errors)
    
    def delete(self,request,id):
        fetch_student=StudentModel.objects.get(id=id)
        fetch_student.delete()
        return Response("Student Deleted")