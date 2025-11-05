from django.urls import path
from .views import *

urlpatterns=[
    path('laptop/',LaptopView.as_view()),
    path('laptop/<int:pk>/',LaptopViewByid.as_view())
]