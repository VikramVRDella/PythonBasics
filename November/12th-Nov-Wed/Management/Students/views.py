from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

class StudentAPI(APIView):
    permission_classes=[IsAuthenticated]

    def get(self,request,id=None):
        if id == None:
            all_student=Student.objects.all()
            fetch_students=Student_Serializer(all_student,many=True).data
            return Response(fetch_students)
        else:
            one_student=Student.objects.get(id=id)
            one_fetch=Student_Serializer(one_student).data
            return Response(one_fetch)
    def post(self,request):
        new_student=Student_Serializer(data=request.data)
        if new_student.is_valid():
            new_student.save()
            return Response("New Student Created")
        else:
            return Response(new_student.errors)
    
    def put(self,request,id):
        fetch_student=Student.objects.get(id=id)
        update_student=Student_Serializer(fetch_student,data=request.data,partial=True)
        if update_student.is_valid():
            update_student.save()
            return Response("Student Details Updated")
        else:
            return Response(update_student.errors)
    
    def delete(self,request,id):
        delete_student=Student.objects.get(id=id)
        delete_student.delete()
        return Response("Student Deleted")
