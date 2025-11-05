from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Persons
from .models import Task
from .serializers import *

class PersonAPI(APIView):

    def get(self, request):

        all_persons=Persons.objects.all()

        person_list=[]

        for i in all_persons:
            person_dict={
                'id':i.id,
                'name':i.name,
                'age':i.age,
            }
            person_list.append(person_dict)

        return Response(person_list)

    def post(self, request):

        new_persons=Persons(name=request.data['name'],age=request.data['age'])

        new_persons.save()

        return Response("New Person Created...")

    def put(self,request,person_id):


        person_data=Persons.objects.filter(id = person_id)

        person_data.update(name=request.data['name'],age=request.data['age'])
        
        return Response("Data Updated")
    
    def delete(self,request,person_id):

        person_data=Persons.objects.get(id=person_id)

        person_data.delete()

        return Response("Person Data Deleted....")

class TaskAPI(APIView):
     def get(self,request,task_id=None):
        if task_id==None:
            all_task=Task.objects.all()
            task_data=TaskSerializer(all_task, many=True).data
            return Response(task_data)
        else:
            task=Task.objects.get(id=task_id)
            task_data=TaskSerializer(task).data
            return Response(task_data)

     def post(self,request):
        new_task=TaskSerializer(data=request.data)
        if new_task.is_valid():
            new_task.save()
            return Response("New Task Pushed...")
        else:
            return Response(new_task.errors)
    
     def patch(self,request,task_id):

        task=Task.objects.get(id=task_id)
        task_data=TaskSerializer(task,data=request.data,partial=True)

        if task_data.is_valid():
            task_data.save()
            return Response("Task Updated...")
        else:
            return Response(task_data.errors)
          
     def delete(self,request,task_id):

        task=Task.objects.get(id=task_id)
        task.delete()
        return Response("Deleted...")
     
class RankViewAPI(APIView):
    def get(self,request,id=None):
        if id==None:
            all=RankModel.objects.all()
            rank_data=RankSerializer(all,many=True).data
            return Response(rank_data)
        else:
            rank=RankModel.objects.get(id=id)
            rank_data=RankSerializer(rank).data
            return Response(rank_data)

    def post(self, request):
        total_mark = (
        request.data['tamil']
        + request.data['english']
        + request.data['maths']
        + request.data['science']
        + request.data['social']
        )
        average_mark = total_mark / 5

        student_result = all([
        request.data['tamil'] > 35,
        request.data['english'] > 35,
        request.data['maths'] > 35,
        request.data['science'] > 35,
        request.data['social'] > 35,
        ])

        data = {
        'tamil': request.data['tamil'],
        'english': request.data['english'],
        'maths': request.data['maths'],
        'science': request.data['science'],
        'social': request.data['social'],
        'total': total_mark,
        'average': average_mark,
        'result': student_result,
        }

        serializer = RankSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response("Data Saved....")
        else:
            return Response(serializer.errors, status=400)



