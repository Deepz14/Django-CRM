from django.urls import path
from . views import register, login_page, logoutUser 

urlpatterns = [ 
    path('register/', register, name="register"),
    path('login/', login_page, name="login"),
    path('logout/', logoutUser, name="logout-user"),
]