from django.urls import path
from . import views

urlpatterns = [  
    path('', views.customerList, name="customer-List"),
    path('add-customer/', views.createCustomer, name="add-customer"),
    path('view-customer/<str:pk>/', views.viewCustomer, name="view-customer"),
]