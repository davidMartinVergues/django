from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.home, name='my-home'),
    path('register/', views.register, name='my-register'), 
]
