from django.urls import path
from .views import *


urlpatterns=[
    path("api/",BookView.as_view())
]
