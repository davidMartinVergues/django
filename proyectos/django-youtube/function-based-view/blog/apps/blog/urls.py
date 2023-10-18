from django.urls import path
from .views import *

urlpatterns = [
    path('',Home, name='index'),
    path('base/',Base, name='base'),
    path('programacion/',Programacion, name='programacion'),
    path('tutoriales/',Tutoriales, name='tutoriales'),
    path('videojuegos/',Videojuegos, name='videojuegos'),
    path('tecnologia/',Tecnologia, name='tecnologia'),
    path('<slug:slug>', postDetail, name='post-detail' )
]
