from django.urls import path,include

from rest_framework.routers import DefaultRouter
from .views import *

router=DefaultRouter()
router.register('stu',StudentView)
router.register('cr',CourseView)

urlpatterns=[
    path('',include(router.urls)),
]