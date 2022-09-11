from operator import mod
from pickle import TRUE
from pyexpat import model
from statistics import mode
from unicodedata import category
from django.db import models

class RestaurantProfile(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=True)
    number_of_tables = models.IntegerField(default=1)
    phone = models.CharField(max_length=10, null=False)
    address = models.CharField(max_length=255, null=True)
    gstn = models.CharField(max_length=100, null=True)
    pan = models.CharField(max_length=100, null=True)
    instagram = models.CharField(max_length=100, null=True)
    facebook = models.CharField(max_length=100, null=True)
    website = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    email = models.EmailField()

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.name


class TaxSlab(models.Model):
    tax_slab = models.IntegerField()

    def __str__(self):
        return self.tax_slab


class Product(models.Model):
    name = models.CharField(primary_key=True, max_length=100, null=False)
    slab = models.ForeignKey(TaxSlab, on_delete=models.DO_NOTHING, null=True, related_name='slab')
    price = models.IntegerField()
    category = models.ForeignKey(ProductCategory, on_delete=models.DO_NOTHING, related_name='category')

    def __str__(self):
        return self.name


class Bill(models.Model):
    id = models.UUIDField(auto_created=True, primary_key=True, null=False)
    restaurant = models.ForeignKey(RestaurantProfile, on_delete=models.CASCADE)
    amount = models.IntegerField()
    items = models.ForeignKey(Product, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.id


class Customer(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True, null=False)
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    restaurant = models.ManyToManyField(RestaurantProfile)

    def __str__(self):
        return self.name