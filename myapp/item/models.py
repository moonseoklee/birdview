from django.db import models

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=32)
    oily = models.CharField(max_length=2)
    dry = models.CharField(max_length=2)
    sensitive = models.CharField(max_length=2)

class Item(models.Model):    
    imageId = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    gender = models.CharField(max_length=6)
    category = models.CharField(max_length=20)
    ingredients = models.CharField(max_length=100)
    monthlySales = models.CharField(max_length=20)
    forOily = models.IntegerField()
    forDry = models.IntegerField()
    forSensitive = models.IntegerField()

