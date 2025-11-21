from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.db.models import Count

class BookView(APIView):
    def get(self,request):
        # # author=AuthorModel.objects.filter(name="Ben")
        # # author=AuthorModel.objects.filter(books__published_year=2023)
        # author=AuthorModel.objects.annotate(book_count=Count('books'))
        # # data=AuthorSerializer(author,many=True).data
        # for i in author:
        #     print(i.name,i.book_count)
        # return Response("Data Fetched On Console")

        # book = BookModel.objects.all()
        # book = BookModel.objects.filter(author__name="William")
        book = BookModel.objects.get(id=3)
        # data=BookSerializer(book,many=True).data
        print(book.title)
        print(book.author.name)
        return Response()