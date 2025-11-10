from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class TodoAPI(APIView):
    def get(self,request,task_id=None):

        if task_id==None:
            all_tasks=TodoModel.objects.all()
            tasks_data=Todo_Serializers(all_tasks,many=True).data
            return Response(tasks_data)
        else:
            one_task=TodoModel.objects.get(id=task_id)
            task_data=Todo_Serializers(one_task).data
            return Response(task_data)
        
    def post(self,request):

        task_insert=Todo_Serializers(data=request.data)
        if task_insert.is_valid():
            task_insert.save()
            return Response("New Task Inserted")
        else:
            return Response(task_insert.errors)
    
    def patch(self,request,task_id):

        fetch_task=TodoModel.objects.get(id=task_id)
        update_task=Todo_Serializers(fetch_task,data=request.data,partial=True)
        if update_task.is_valid():
            update_task.save()
            return Response("New Task Updated")
        else:
            return Response(update_task.errors)
    
    def delete(self,request,task_id):
        delete_task=TodoModel.objects.get(id=task_id)
        delete_task.delete()
        return Response("Task Deleted")


