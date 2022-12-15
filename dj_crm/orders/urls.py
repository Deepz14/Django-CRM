from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.orderList, name="order-List"),
    path('view-order/<str:pk>/', views.viewOrder, name="view-order"),
    path('edit-order/<str:pk>/', views.updateOrder, name="edit-order"),
    path('delete-order/<str:pk>/', views.deleteOrder, name="delete-order"),
]