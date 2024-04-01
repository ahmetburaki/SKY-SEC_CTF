from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Product(models.Model):
    date = models.DateField()
    popularity = models.IntegerField()
    rating = models.IntegerField()
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    img_name = models.CharField(max_length=100)


class Cart(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)