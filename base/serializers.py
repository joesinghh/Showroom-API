from dataclasses import fields
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.models import User
from .models import Bikes, Order

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ["id", "username", "is_staff"]


class RegisterSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(
    required=True,
    validators=[UniqueValidator(queryset=User.objects.all())]
  )
  password = serializers.CharField(
    write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ('username', 'password', 'password2',
         'email', 'is_staff')
    extra_kwargs = {
      'is_staff': {'required': True},

    }
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError(
        {"password": "Passwords don't match"})
    return attrs
  def create(self, data):
    user = User.objects.create(
      username=data['username'],
      email=data['email'],
      is_staff=data['is_staff']
    )
    user.set_password(data['password'])
    user.save()
    return user

class BikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Bikes
    fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
  class Meta:
    model = Order
    fields = '__all__'

