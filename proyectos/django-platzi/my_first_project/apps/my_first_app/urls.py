
from django.urls import path
from .views import get_cars

apps_name = 'my_first_app'

urlpatterns = [
    path('car_list/', get_cars, name="get_cars" ),
]