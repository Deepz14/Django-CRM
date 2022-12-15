from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from . forms import CustomUserCreationForm

def register(request):
    if request.user.is_authenticated:
        return redirect('product-List')
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            login(user)
            return redirect('product-List')
        else:
            return HttpResponseBadRequest('Bad Request')    

    context = {'form': form}
    return render(request, 'users/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('product-List')
    form = CustomUserCreationForm()
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        try:
            login_user = User.objects.get(email=email)
        except Exception as e:
            return HttpResponseBadRequest('User not exist') 
        user = authenticate(request, username=login_user, password=password)
        if user is not None:
            print('user', user)
            login(request, user)
            return redirect('product-List')
        else:
            return HttpResponseBadRequest('username or password is incorrect!')

    context = {'form': form}
    return render(request, 'users/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')
