from django.db import models
from food.models import Food

class Order (models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    price = models.IntegerField()
    username = models.TextField()
    orderNumber = models.IntegerField()