from rest_framework import generics
from .models import *
from .serializers import *

class LaptopView(generics.ListCreateAPIView):
    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer

class LaptopViewByid(generics.RetrieveUpdateDestroyAPIView):
    queryset=Laptop.objects.all()
    serializer_class=LaptopSerializer