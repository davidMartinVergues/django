from django.shortcuts import render

from .models import Car
# Create your views here.


def get_cars(request):
    cars = Car.objects.all()

    context = {
        "data_cars": cars
    }

    return render(request,'my_first_app/car_list.html', context=context)

