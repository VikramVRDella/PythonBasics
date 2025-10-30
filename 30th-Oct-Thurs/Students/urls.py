from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns=[
    path("details/",PersonAPI.as_view()),
    path("details/<int:person_id>/",PersonAPI.as_view()),
    path("task/",TaskAPI.as_view()),
    path("task/<int:task_id>/",TaskAPI.as_view()),
    path("rank/",RankViewAPI.as_view()),
    path("rank/<int:id>/",RankViewAPI.as_view())
]