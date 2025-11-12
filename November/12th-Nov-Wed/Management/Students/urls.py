from django.urls import path
from .views import *

urlpatterns=[
    path('student/',StudentAPI.as_view()),
    path('student/<int:id>',StudentAPI.as_view()),
]