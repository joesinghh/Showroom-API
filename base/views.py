from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BikeSerializer, UserSerializer,RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from .models import *

class UserDetailAPI(APIView):
  authentication_classes = (TokenAuthentication,)
  permission_classes = (AllowAny,)
  def get(self,request,*args,**kwargs):
    user = User.objects.get(id=request.user.id)
    serializer = UserSerializer(user)
    return Response(serializer.data)


class RegisterUserAPIView(generics.CreateAPIView):
  permission_classes = (AllowAny,)
  serializer_class = RegisterSerializer

@api_view(['GET', 'POST'])
def bikes(request):
  
  if request.method== 'GET':
    bikes= Bikes.objects.all()
    serilazer = BikeSerializer(bikes, many=True)
    return Response(serilazer.data,)

  elif request.method == 'POST':
    if request.user.is_staff:
      serilazer = BikeSerializer(data=request.data)
      if serilazer.is_valid():
        serilazer.save()
        return Response(serilazer.data, status=status.HTTP_201_CREATED)

    else:
      return Response({"ERROR ": "Only Staff can add bikes"},status=status.HTTP_404_NOT_FOUND )


      


