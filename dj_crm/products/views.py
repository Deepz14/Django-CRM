from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . forms import ProductForm
from . models import Product

# Create your views here.
def productsList(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'products/products.html', context)

@login_required(login_url='login')
def createProduct(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully.')
            return redirect('product-List') 
    else:
        form = ProductForm()
    context = {'form': form, 'page': 'Add Product'}
    return render(request, 'products/product_form.html', context)  

def viewProduct(request, pk):
    product = Product.objects.get(id=pk)
    category = product.category.all()
    context = {'product': product, 'categorys': category}
    return render(request, 'products/product_detail.html', context)
    
@login_required(login_url='login')
def updateProduct(request, pk):
    product = Product.objects.get(id=pk)
    form = ProductForm(instance=product)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product updated successfully.')
            return redirect('product-List') 
    context = {'form': form, 'page': 'Edit Product'}
    return render(request, 'products/product_form.html', context)

@login_required(login_url='login')
def deleteProduct(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, 'Product deleted successfully.')
        return redirect('product-List')
    context = {'obj': product}
    return render(request, 'products/delete_product.html', context)    
        
