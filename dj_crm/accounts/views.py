from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth import get_user_model
from . forms import RegisterForm, LoginUserForm

User = get_user_model()

# Create your views here.
def register(request):
    if request.user.is_authenticated:
        return redirect('product-List')
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data.get('password1')
            user.set_password(password)
            user.save()

            login(request, user)
            return redirect('product-List')
        else:
            return HttpResponseBadRequest('Bad Request')    
    form = RegisterForm()
    context = {'form': form}
    return render(request, 'accounts/register.html', context)

def login_page(request):
    if request.user.is_authenticated:
        return redirect('product-List')
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password1']
        try:
            login_user = User.objects.get(email=email)
        except Exception as e:
            return HttpResponseBadRequest('User not exist') 
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('product-List')
        else:
            return HttpResponseBadRequest('username or password is incorrect!')
    form = LoginUserForm()
    context = {'form': form}
    return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')