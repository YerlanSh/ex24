from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import client_detail

urlpatterns = [
    path('clients/', client_detail, name='client_detail'),
]