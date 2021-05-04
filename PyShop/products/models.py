from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=256)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)

    def __str__(self):
        return self.name


class Offer(models.Model):
    code = models.CharField(max_length=10)
    decription = models.CharField(max_length=256)
    discount = models.FloatField()

    def __str__(self):
        return self.code