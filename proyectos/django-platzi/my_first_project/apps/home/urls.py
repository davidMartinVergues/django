
from django.urls import path

from .views import home

apps_name= 'home'

urlpatterns = [
    path('',home,name='home')
]