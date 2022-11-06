from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BikeSerializer, UserSerializer,RegisterSerializer, OrderSerializer
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import *
from datetime import datetime

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

@api_view(['GET', ])
def bikes(request):
  
  if request.method== 'GET':
    bikes= Bikes.objects.all()
    serilazer = BikeSerializer(bikes, many=True)
    return Response(serilazer.data,)

@api_view(['POST', ])
@permission_classes([IsAuthenticated, IsAdminUser])
def addbikes(request):
  if request.method == 'POST':
    serilazer = BikeSerializer(data=request.data)
    if serilazer.is_valid():
      serilazer.save()
      return Response(serilazer.data, status=status.HTTP_201_CREATED)
    return Response(serilazer.errors, status=status.HTTP_404_BAD_REQUEST)

@api_view(['PUT','DELETE' ])
@permission_classes([IsAuthenticated, IsAdminUser])
def modbikes(request, id):
  try:
    obj = Bikes.objects.get(pk=id)
  except Bikes.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method=='PUT':
    serilazer = BikeSerializer(data=request.data)
    if serilazer.is_valid():
      serilazer.save()
      return Response(serilazer.data)
    return Response(serilazer.errors, status=status.HTTP_400_BAD_REQUEST)

  elif request.method=='DELETE':
    obj.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
  
@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated, ])
def order(request, ):
  if request.method=='POST':

    serilazer = OrderSerializer(data=request.data)
    if serilazer.is_valid():
      serilazer.save()
      return Response(serilazer.data, status=status.HTTP_201_CREATED)
    return Response(serilazer.errors, status=status.HTTP_404_NOT_FOUND)

  elif request.method== 'GET':
    orders= Order.objects.all()
    serilazer = OrderSerializer(orders, many=True)
    return Response(serilazer.data,)

@api_view(['GET', ])
@permission_classes([IsAuthenticated, ])
def orderdetail(request, id):
  try:
    obj = Order.objects.get(pk=id)
  except Order.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  warranty = Bikes.objects.get(modelnumber=obj.bike).warranty
  time = obj.date
  time = time.replace(tzinfo=None)
  # time = time.strftime("%Y-%m-%d")
  now = datetime.now()
  now = now.replace(tzinfo=None)
  # now = now.strftime("%Y-%m-%d")

  days = now-time
  if warranty>days.days:
    msg = f'{days.days} days left'
  else:
    msg = f'Warranty over'
  serializer = OrderSerializer(obj)
  data = serializer.data
  data['Warranty Status'] = msg
  return Response(data, status=status.HTTP_200_OK)
