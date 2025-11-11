from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class StudentAPI(APIView):
    
    def get(self,request,student_id=None):
        if student_id==None:
            all_students=Student.objects.all()
            students_data=Student_Data_Serializer(all_students,many=True).data
            return Response(students_data)
        else:
            one_student=Student.objects.get(id=student_id)
            student_data=Student_Data_Serializer(one_student).data
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

class TaskAPI(APIView):
    def get(self,request,task_id=None):
        if task_id==None:
            all_task=Task.objects.all()
            Task_data=Task_Data_Serializer(all_task,many=True).data
            return Response(Task_data)
        else:
            one_student=Task.objects.get(id=task_id)
            task_data=Task_Data_Serializer(one_student).data
            return Response(task_data)
    
    def post(self,request):
        task_data=Task_Serializer(data=request.data)
        if task_data.is_valid():
            task_data.save()
            return Response("New Data Added")
        else:
            return Response(task_data.errors)
    
    def patch(self,request,task_id):

        fetch_task=Task.objects.get(id=task_id)
        update_task=Task_Serializer(fetch_task,data=request.data,partial=True)
        if update_task.is_valid():
            update_task.save()
            return Response("New Task Updated")
        else:
            return Response(update_task.errors)
    
    def delete(self,request,task_id):
        delete_task=Task.objects.get(id=task_id)
        delete_task.delete()
        return Response("Task Deleted")
            
