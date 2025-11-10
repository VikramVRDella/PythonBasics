from django.urls import path
from .views import *
urlpatterns=[
    path('api/',BmiAPI.as_view()),
    path('api/<int:bmi_id>',BmiAPI.as_view())
]