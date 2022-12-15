from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product, Order
from customers.forms import OrderForm

# Create your views here.
@login_required(login_url='login')
def createOrder(request, pk):
    product = Product.objects.get(id=pk)
    form = OrderForm()
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.product = product

            order.save()
            product.stock_update
            return redirect('product-List')
    context = {'form': form, 'product': product}
    return render(request, 'orders/order_form.html', context)

@login_required(login_url='login')
def orderList(request):
    orders = Order.objects.all().order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'orders/orders.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == "POST":
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.save()
            return redirect('product-List')
    context = {'form': form, 'product': order.product}
    return render(request, 'orders/order_form.html', context)
    

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        if order is not None:
            order.delete()
            return redirect('order-List')
    return render(request, 'orders/delete_order.html', {'obj': order})