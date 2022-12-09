from django.shortcuts import render, redirect
from django.contrib import messages
from . forms import ProductForm
from . models import Product

# Create your views here.
def productsList(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)

def createProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('product-List') 
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'products/product_form.html', context)  

def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    category = product.category.all()
    context = {'product': product, 'categorys': category}
    return render(request, 'products/product_detail.html', context)

def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product-List')
    context = {'obj': product}
    return render(request, 'products/delete_product.html', context)    
        
