from django.urls import path,include
from .router import library_route

urlpatterns=[
    path('api/',include(library_route.urls))
]