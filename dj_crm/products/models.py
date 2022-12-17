import uuid
from django.db import models
from customers.models import Customer
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.name
        
class Category(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.name  

class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField(max_length=200, null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    rating = models.DecimalField(default=0, max_digits=3, decimal_places=1)
    comment = models.TextField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    @property
    def stock_update(self):
        self.stock -= 1
        self.save()


    def __str__(self) -> str:
        return self.name


class Order(models.Model):
    STATUS_OPTIONS = [
        ('ordered', 'Ordered'),
        ('outfordelivery', 'Out For Delivery'),
        ('delivered', 'Delivered')
    ]
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    status = models.CharField(max_length=100, choices=STATUS_OPTIONS)
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)

    def __str__(self) -> str:
        return self.product.name