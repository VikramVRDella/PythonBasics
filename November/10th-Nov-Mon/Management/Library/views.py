from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.decorators import api_view

class BookView(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=Book_Serializer

class LaptopView(generics.ListCreateAPIView):
    def perform_create(self, serializer):
        serializer.save(user_type="Low Performance")

    queryset=Laptop.objects.all()
    serializer_class=Laptop_Serializer

class LaptopViewByID(generics.RetrieveUpdateDestroyAPIView):
    def perform_update(self, serializer):
        serializer.save(user_type="High Perfromance")
    queryset=Laptop.objects.all()
    serializer_class=Laptop_Serializer

