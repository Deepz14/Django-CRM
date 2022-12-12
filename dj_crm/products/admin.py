from django.contrib import admin
from . models import Category, Product, Brand, Order
# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Brand)
admin.site.register(Order)
