from django.contrib import admin
from .models import Bikes, Order, Category

admin.site.register(Bikes)
admin.site.register(Order)
admin.site.register(Category)