from django.urls import path
from .views import home,login,back

urlpatterns = [
    path('',home),
    path('login.html',login),
    path('home.html',back)
]