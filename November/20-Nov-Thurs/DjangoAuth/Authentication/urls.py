from django.urls import path
from .views import *


urlpatterns=[
    path('api/',TestAPI.as_view()),
]