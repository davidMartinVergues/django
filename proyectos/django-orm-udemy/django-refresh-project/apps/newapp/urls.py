
from django.urls import path, include
from . import views


apps_name='newapp' 

urlpatterns = [
    path("",views.home, name='home'),
]
