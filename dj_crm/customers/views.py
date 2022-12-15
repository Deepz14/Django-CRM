from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . models import Customer
from . forms import CustomerForm

# Create your views here.
def customerList(request):
    customers = Customer.objects.all()
    context = {'cutomers': customers}
    return render(request, 'customers/customers.html', context)

@login_required(login_url='login')
def createCustomer(request):
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Customer added successfully.')
            return redirect('customer-List')

    context = {'form': form, 'page': 'Add Customer'}
    return render(request, 'customers/customer_form.html', context)


@login_required(login_url='login')
def viewCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all().order_by('-created_at')[:5]
    context = {'customer': customer, 'orders': orders}
    return render(request, 'customers/customer_detail.html', context)

@login_required(login_url='login')
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('customer-List')
    context = {'form': form, 'page': 'Edit Customer'}
    return render(request, 'customers/customer_form.html', context)


@login_required(login_url='login')
def deleteCutomer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('customer-List')
    context = {'obj': customer}
    return render(request, 'customers/delete_customer.html', context)  
