from django.shortcuts import render, redirect
from django.contrib import messages
from . models import Customer
from . forms import CustomerForm

# Create your views here.
def customerList(request):
    customers = Customer.objects.all()
    context = {'cutomers': customers}
    return render(request, 'customers/customers.html', context)

def createCustomer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer added successfully.')
            return redirect('customer-List')

    context = {'form': form}
    return render(request, 'customers/customer_form.html', context)

def viewCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all().order_by('-created_at')[:5]
    context = {'customer': customer, 'orders': orders}
    return render(request, 'customers/customer_detail.html', context)

def updateCustomer(request):
    pass

def deleteCutomer(request):
    pass
