from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.orderList, name="order-List"),
    path('create-order/<str:pk>/', views.createOrder, name="create-order"),
    path('edit-order/<str:pk>/', views.updateOrder, name="edit-order"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="delete-order"),
]