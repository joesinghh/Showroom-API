from django.urls import path
from .views import *

urlpatterns = [
    path("profile",UserDetailAPI.as_view()),
    path('register',RegisterUserAPIView.as_view()),
    path('bikes',bikes),
    path('addbike', addbikes),
    path('bikes/<int:id>', modbikes),
    path('order', order),
    path('order/<int:id>',orderdetail )

]