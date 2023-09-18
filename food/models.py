from django.db import models

class Food (models.Model):
    name = models.TextField()
    price = models.IntegerField()
    img = models.TextField()
    description = models.TextField()