from django.db import models

class Drink (models.Model):
    name = models.TextField()
    price = models.IntegerField()
    img = models.TextField()
    description = models.TextField()