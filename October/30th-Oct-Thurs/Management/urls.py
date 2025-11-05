
from django.contrib import admin
from django.urls import path,include
from Students.views import PersonAPI
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',include("Students.urls")),
]
