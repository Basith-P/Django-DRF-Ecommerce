from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True)


class Brand(models.Model):
    name = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    # slug = models.SlugField(max_length=255, unique=True)
    description = models.TextField(blank=True)
    is_digital = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
