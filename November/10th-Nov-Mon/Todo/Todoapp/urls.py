from django.urls import path
from .models import TodoModel
from .views import TodoAPI

urlpatterns=[
    path('api/',TodoAPI.as_view()),
    path('api/<int:task_id>',TodoAPI.as_view())
]