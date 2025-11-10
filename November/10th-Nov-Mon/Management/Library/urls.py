from django.urls import path,include
from .router import library_router
from .views import *

urlpatterns=[
   path('book/',include(library_router.urls)),
   path('laptop/',LaptopView.as_view()),
   path('laptop/<int:pk>/',LaptopViewByID.as_view())

]