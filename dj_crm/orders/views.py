from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from products.models import Product, Order

# Create your views here.
def orderList(request):
    orders = Order.objects.all().order_by('-created_at')
    context = {'orders': orders}
    return render(request, 'orders/orders.html', context)

def viewOrder(request):
    pass

def updateOrder(request):
    pass

def deleteOrder(request):
    pass