from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.productsList, name="product-List"),
    path('add-product/', views.createProduct, name="add-product"),
    path('view-product/<str:pk>/', views.viewProduct, name="view-product"),
    path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),
]