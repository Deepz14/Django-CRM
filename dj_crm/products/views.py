from django.shortcuts import render

# Create your views here.
def productsList(request):
    return render(request, 'products/products.html')
