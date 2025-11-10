from django.urls import path
from .views import *

urlpatterns=[
    path('api/',StudentAPI.as_view()),
    path('api/<int:student_id>',StudentAPI.as_view()),
    path('api/list/create/',student_get_post),
    path('api/update/delete/<int:student_id>/',student_put_delete),
]