from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length = 200)
    items = models.IntegerField()
    
    def __str__(self):
        return f'{self.name}'

class Bikes(models.Model):
    modelnumber = models.CharField(max_length = 200)
    price  = models.IntegerField()
    warranty = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length = 20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.modelnumber}'

class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bikes, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.id}'



