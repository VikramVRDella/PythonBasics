from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Student
from .serializers import Student_Serializer
from rest_framework.decorators import api_view

class StudentAPI(APIView):
    
    def get(self,request,student_id=None):
        if student_id==None:
            all_students=Student.objects.all()
            students_data=Student_Serializer(all_students,many=True).data
            return Response(students_data)
        else:
            one_student=Student.objects.get(id=student_id)
            student_data=Student_Serializer(one_student).data
            return Response(student_data)
    
    def post(self,request):
        new_students=Student_Serializer(data=request.data)
        if new_students.is_valid():
            new_students.save()
            return Response("New Student Added")
        else:
            return Response(new_students.errors)
    
    def patch(self,request,student_id):
        fetch_student=Student.objects.get(id=student_id)
        update_student=Student_Serializer(fetch_student,data=request.data,partial=True)

        if update_student.is_valid():
            update_student.save()
            return Response("Student Updated")
        else:
            return Response(update_student.errors)

    def delete(self,request,student_id):
        delete_data=Student.objects.get(id=student_id)
        delete_data.delete()
        return Response("Student Deleted..")

@api_view(['GET','POST'])
def student_get_post(request):
    if request.method == 'GET':
         all_students=Student.objects.all()
         students_data=Student_Serializer(all_students,many=True).data
         return Response(students_data)
    elif request.method == 'POST':
        new_students=Student_Serializer(data=request.data)
        if new_students.is_valid():
            new_students.save()
            return Response("New Student Added")
        else:
            return Response(new_students.errors)

@api_view(['GET','PATCH','PUT','DELETE'])
def student_put_delete(request,student_id):
    student=Student.objects.get(id=student_id)
    if request.method == 'GET':
         student_data=Student_Serializer(student).data
         return Response(student_data)
    elif request.method == "PATCH":
        update_student=Student_Serializer(student,data=request.data,partial=True)

        if update_student.is_valid():
            update_student.save()
            return Response("Student Updated")
        else:
            return Response(update_student.errors)
    elif request.method == "PUT":
        update_student=Student_Serializer(student,data=request.data,partial=True)

        if update_student.is_valid():
            update_student.save()
            return Response("Student Updated")
        else:
            return Response(update_student.errors)
    elif request.method == 'DELETE':
        student.delete()
        return Response("Student Deleted..")