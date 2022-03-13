from django.shortcuts import render
from .models import Post, Categoria

# Create your views here.

def Home(request):
    posts= Post.objects.filter(estado=True)

    return render(request,'index.html', {'posts':posts})


def Base(request):
    
    return render(request,'base.html',{'posts':Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='General'))})

def Programacion(request):
    return render(request,'programacion.html',{'posts':Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='programacion'))})

def Tutoriales(request):
    return render(request,'tutoriales.html',{'posts':Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='tutoriales'))})

def Tecnologia(request):
    return render(request,'tecnologia.html',{'posts':Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='tecnologia'))})

def Videojuegos(request):
    return render(request,'videojuegos.html',{'posts':Post.objects.filter(estado=True,categoria= Categoria.objects.get(nombre='videojuegos'))})

def postDetail(request,slug):

    post = Post.objects.get(slug = slug)
    
    return render(request,'post.html', {'post_detail':post})