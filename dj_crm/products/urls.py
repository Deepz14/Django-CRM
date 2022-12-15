from django.urls import path
from . import views

urlpatterns = [
    path('', views.productsList, name="product-List"),
    path('add-product/', views.createProduct, name="add-product"),
    path('view-product/<str:pk>/', views.viewProduct, name="view-product"),
    path('edit-product/<str:pk>/', views.updateProduct, name="edit-product"),
    path('delete-product/<str:pk>/', views.deleteProduct, name="delete-product"),
]