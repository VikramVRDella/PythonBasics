from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from decouple import config

class StudentAPI(APIView):
    def get(self,request,id=None):
        if id==None:
            Pname=config("name")
            print(Pname)
            all_student=StudentModel.objects.all()
            fetch_student=StudentSerializer(all_student,many=True).data
            return Response(fetch_student)
        else:
            one_student=StudentModel.objects.get(id=id)
            fetch=StudentSerializer(one_student).data
            return Response(fetch)
    
    def post(self,request):
        create_students=StudentSerializer(data=request.data)
        if create_students.is_valid():
            create_students.save()
            return Response("New Student Created")
        else:
            return Response(create_students.errors)
    
    def put(self,request,id):
        one_fetch=StudentModel.objects.get(id=id)
        update_student=StudentSerializer(one_fetch,data=request.data,partial=True)
        if update_student.is_valid():
            update_student.save()
            return Response(f"ID No : {id} is Updated")
        else:
            return Response(update_student.errors)
    
    def delete(self,request,id):
        one=StudentModel.objects.get(id=id)
        one.delete()
        return Response("Student Deleted")