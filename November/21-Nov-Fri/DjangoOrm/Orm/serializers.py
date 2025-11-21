from rest_framework.serializers import ModelSerializer
from .models import *

class BookSerializer(ModelSerializer):
    class Meta:
        model=BookModel
        fields='__all__'
class AuthorSerializer(ModelSerializer):
    class Meta:
        model=AuthorModel
        fields='__all__'
class AuthorwithBookSerializer(ModelSerializer):
    books=BookSerializer(many=True)
    class Meta:
        model=AuthorModel
        fields='__all__'
class BookwithAuthorSerializer(ModelSerializer):
    author=AuthorSerializer()
    class Meta:
        model=BookModel
        fields='__all__'