from django.urls import path
from .views import *

urlpatterns=[
    path('student/',StudentAPI.as_view()),
    path('student/<int:student_id>/',StudentAPI.as_view()),
    path('task/',TaskAPI.as_view()),
    path('task/<int:task_id>/',TaskAPI.as_view())
]