from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from products.models import Product, Order

# Create your views here.
@login_required(login_url='login')
def orderList(request):
    orders = Order.objects.all().order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'orders/orders.html', context)

def viewOrder(request):
    pass

def updateOrder(request):
    pass

@login_required(login_url='login')
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        if order is not None:
            order.delete()
            return redirect('order-List')
    return render(request, 'orders/delete_order.html', {'obj': order})