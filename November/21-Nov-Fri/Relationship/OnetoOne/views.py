from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

class ProfileView(ModelViewSet):
    queryset=ProfileModel.objects.all()
    serializer_class=ProfileSerializer

class Profile(APIView):
    def post(self,request):
        try:
            new_profile=ProfileModel(user_id=request.data['user'],bio=request.data['bio'])
            new_profile.save()
            return Response("Profile Created..")
        except:
            return Response("The User has the Profile")