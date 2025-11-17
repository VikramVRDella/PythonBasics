from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *


class BookView(ModelViewSet):
    queryset=Book.objects.all()
    serializer_class=Book_Serializer
