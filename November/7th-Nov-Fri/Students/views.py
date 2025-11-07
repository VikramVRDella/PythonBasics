from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *


class StudentAPI(APIView):

    def get(self,request):
        all_students=Student.objects.all()
        stu_list=[]        
        for i in all_students:

            stu_dict={
                "id":i.id,
                "name":i.name,
                "age":i.age
            }
            stu_list.append(stu_dict)

        return Response(stu_list)
    
    def post(self,request):
        print(request.data)
        new_student=Student(id=request.data['id'],name=request.data['name'],age=request.data['age'])
        new_student.save()
        return Response('New Data Created')
    
    def patch(self,request,stu_id):
        stu_obtain=Student.objects.filter(id=stu_id)
        stu_obtain.update(name=request.data['name'],age=request.data['age'])
        return Response("Student Data Updated")
    def put(self,request,stu_id):
        stu_obtain=Student.objects.filter(id=stu_id)
        stu_obtain.update(name=request.data['name'],age=request.data['age'])
        return Response("Student Data Updated")
    def delete(self,request,stu_id):
        stu_obtain=Student.objects.get(id=stu_id)
        stu_obtain.delete()
        return Response("Student Data Deleted")

class TaskAPI(APIView):

    def get(self,request,task_id=None):
        if task_id==None:
            task_get=Task.objects.all()
            task_data=Task_Serializer(task_get,many=True).data
            return Response (task_data)
        else:
            task_one=Task.objects.get(id=task_id)
            task_res=Task_Serializer(task_one).data
            return Response(task_res)

    def post(self,request):
        new_task=Task_Serializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("New Task Added")
        else:
            return Response(new_task.errors)
        
    def put(self,request,task_id):
        task=Task.objects.get(id=task_id)
        task_update=Task_Serializer(task,data=request.data,partial=True)
        if task_update.is_valid():
            task_update.save()
            return Response("Updated Task Added")
        else:
            return Response(task_update.errors)
    def patch(self,request,task_id):
        task=Task.objects.get(id=task_id)
        task_update=Task_Serializer(task,data=request.data)
        if task_update.is_valid():
            task_update.save()
            return Response("Updated Task Added")
        else:
            return Response(task_update.errors)
        
    def delete(self,request,task_id):
        task=Task.objects.get(id=task_id)
        task.delete()
        return Response("Task Deleted")
    
class RankAPI(APIView):

    def get(self,request,rank_id=None):
        if rank_id==None:
            ranks=RankSheet.objects.all()
            results=Rank_Serializer(ranks,many=True).data
            return Response(results)
        else:
            rank=RankSheet.objects.get(id=rank_id)
            result=Rank_Serializer(rank).data
            return Response(result)


    def post(self,request):
        total=request.data['tamil']+request.data['english']+request.data['maths']+request.data['science']+request.data['social']
        average=total/5
        
        if(request.data['tamil']>=35) and (request.data['english']>=35) and (request.data['maths']>=35) and (request.data['science']>=35) and (request.data['science']>=35) and (request.data['social']>=35):
            result=True
        else:
            result=False

        new_data=RankSheet(
            tamil=request.data['tamil'],
            english=request.data['english'],
            maths=request.data['maths'],
            science=request.data['science'],
            social=request.data['social'],
            total=total,
            average=average,
            result=result
        )
        new_data.save()

        return Response("Data Saved")
    
    def put(self,request,rank_id):
        rank_edit=RankSheet.objects.filter(id=rank_id)
        total = (
                    request.data['tamil'] +
                    request.data['english'] +
                    request.data['maths'] +
                    request.data['science'] +
                    request.data['social']
                )

        rank_edit.update(
            tamil=request.data['tamil'],
            english=request.data['english'],
            maths=request.data['maths'],
            science=request.data['science'],
            social=request.data['social'],
            total=total,
            average=total / 5,
            result=all([
                request.data['tamil'] >= 35,
                request.data['english'] >= 35,
                request.data['maths'] >= 35,
                request.data['science'] >= 35,
                request.data['social'] >= 35
            ])
        )

        return Response("Rank Sheet Updated")