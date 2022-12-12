from django.shortcuts import render
from . models import Customer
# Create your views here.
def customerList(request):
    customers = Customer.objects.all()
    context = {'cutomers': customers}
    return render(request, 'customers/customers.html', context)

def createCustomer(request):
    pass

def updateCustomer(request):
    pass

def deleteCutomer(request):
    pass
