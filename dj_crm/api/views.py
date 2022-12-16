from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from . serializers import ProductSerializer
from products.models import Product
# Create your views here.

@api_view(['GET', 'POST'])
def product_list_create(request):
  if request.method == 'GET':
      product = Product.objects.all()  # querySet
      serializer = ProductSerializer(product, many=True)
      return Response(serializer.data)
  if request.method == 'POST':
      serializer = ProductSerializer(data=request.data)
      if serializer.is_valid():
         serializer.save() 
         return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):
    def get_product_by_pk(self, pk):
        try:
            product = Product.objects.get(id=pk)
        except:
            return Response({'error': 'Product not found!'}, status=status.HTTP_404_NOT_FOUND)
        return product

    def get(self, request, pk):
        product = self.get_product_by_pk(pk)
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        product = self.get_product_by_pk(pk)
        serializer = ProductSerializer(product, data=request.data)

        if serializer.is_valid():
           serializer.save()
           return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def delete(self, request, pk):
        product = self.get_product_by_pk(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)          
