from django.db import models
from django import forms
import pickle

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    tel = models.CharField(max_length=10, unique=True)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Client name: {self.name}, email: {self.email}, telephone: {self.tel}'

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.ImageField(upload_to='uploads/', default='uploads/default.jpg', blank=True)
    quantity = models.PositiveIntegerField()
    date_insert = models.DateTimeField(auto_now_add=True)

def __str__(self):
        return f'Product name: {self.name}, price: {self.price}, quantity: {self.quantity}'
    
class Order(models.Model):
    customer=models.ForeignKey(Client, on_delete=models.CASCADE)
    products=models.ManyToManyField(Product) 
    total_price=models.DecimalField(max_digits=10,decimal_places=2)
    date_ordered=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order price: {self.total_price}, products: {self.products}, date: {self.date_ordered}'

    def get_all_products(self):
        pass

    def ordering(self):
        pass