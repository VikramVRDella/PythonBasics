from django.urls import path
from .views import *

urlpatterns = [
    path('api/',StudentAPI.as_view()),
    path('api/<int:stu_id>',StudentAPI.as_view()),
    path('taskapi/',TaskAPI.as_view()),
    path('taskapi/<int:task_id>/',TaskAPI.as_view()),
    path('rank/',RankAPI.as_view()),
    path('rank/<int:rank_id>/',RankAPI.as_view())
]
