from django.urls import path
from . import views

urlpatterns = [ 
    path('product/', views.product_list_create, name="product-list"),
    path('product/<str:pk>/', views.ProductDetail.as_view(), name="product-detail")
]