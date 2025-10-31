from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import *

class BookView(ModelViewSet):

    queryset=Books.objects.all()
    serializer_class=BookSerializer