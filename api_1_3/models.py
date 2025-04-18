from django.utils import timezone

from django.db import models
from cloudinary.models import CloudinaryField
class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = CloudinaryField('image', default='')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class Client (models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Order(models.Model):
    code = models.CharField(max_length=200)
    date = models.DateField(default= timezone.now)
    client = models.ForeignKey(Client, on_delete=models.RESTRICT)

class OrderProduct(models.Model):
    order = models.ForeignKey(Order, related_name='order_products',on_delete=models.RESTRICT)
    product = models.ForeignKey(Product, on_delete=models.RESTRICT)
    quantity = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    def __str__ (self):
        return f'{self.product.name} - {self.quantity}'
    