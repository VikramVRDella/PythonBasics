from django.urls import path
from .views import *
urlpatterns=[
    path('api/',Student.as_view()),
]