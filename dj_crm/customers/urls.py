from django.urls import path
from . import views

urlpatterns = [  
    path('', views.customerList, name="customer-List")
]