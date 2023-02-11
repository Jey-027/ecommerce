from django.db import models

# Create your models here.
class Products(models.Model):
    codigo = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    ean = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.codigo, self.name}"

class purchase(models.Model):
    sku = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    customer_name = models.CharField(max_length=50)
    comments = models.TextField()

    def __str__(self):
        return self.customer_name


class Topping(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    topping = models.ForeignKey(Topping, on_delete=models.CASCADE)