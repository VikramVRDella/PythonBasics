from rest_framework.serializers import ModelSerializer
from .models import Task,RankModel

class TaskSerializer(ModelSerializer):
    class Meta:
        model=Task
        fields='__all__'
class RankSerializer(ModelSerializer):
    class Meta:
        model=RankModel
        fields='__all__'