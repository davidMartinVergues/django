from ast import Try, excepthandler
from django.shortcuts import redirect, render, redirect
from django.core.exceptions import ObjectDoesNotExist

from .forms import AutorForm
from .models import Autor

# Create your views here.

def Home(request):
    return render(request,'index.html')


def crearAutor(request):
    autor_form= None
    if request.method == 'POST':

        autor_form = AutorForm(request.POST)

        if autor_form.is_valid():
            print(autor_form.cleaned_data)
            autor_form.save()
            return redirect('index') # utilizamos el name de la url en lugar de la url completa
    else:
        # si lo hacemos así AutorForm genera un HTML con el formulario en base al modelo Autor
        autor_form = AutorForm()
        
    return render(request,'libro/crear_autor.html', {'autor_form':autor_form})

        
def listarAutor(request):
    autor_list = Autor.objects.filter(estado=True)
    return render(request,'libro/listar_autores.html', {'autores':autor_list})

def editarAutor(request,pk):
    autor_form = None
    error = None
    try:
        autor = Autor.objects.get(id=pk)
        if request.method=='GET':
            autor_form = AutorForm(instance=autor) # añade en el form la info del autor recuperado
        else:
            autor_updated = AutorForm(request.POST, instance=autor) # al añadir instance modifica el autor existente si no le pusieramos instance crearía un nuevo autor
            if autor_updated.is_valid():
                autor_updated.save()
            return redirect('libro:listar_autores')
    except ObjectDoesNotExist as e:
        error = e 

    return render(request,'libro/crear_autor_copy.html',{'autor_form':autor_form, 'error':error})

def eliminarAutor(request,pk):

    error = None

    try:
        autor = Autor.objects.get(id=pk)
        autor.delete()
        return redirect('libro:listar_autores')
    except ObjectDoesNotExist as e:
        error = e

    return render(request, 'libro/error-not-found.html', {'error':error,'id':pk})

def eliminarAutorV2(request,pk):

    error = None

    try:
        autor = Autor.objects.get(id=pk)

        if request.method == 'POST':
            autor.delete()
            return redirect('libro:listar_autores')
    except ObjectDoesNotExist as e:
        error = e
        return render(request, 'libro/error-not-found.html', {'error':error,'id':pk})

    return render(request, 'libro/eliminar-autor.html', {'autor':autor})

def eliminarAutorV3(request,pk):

    error = None

    try:
        autor = Autor.objects.get(id=pk)

        if request.method == 'POST':
            autor.estado = False
            autor.save()
            return redirect('libro:listar_autores')
    except ObjectDoesNotExist as e:
        error = e
        return render(request, 'libro/error-not-found.html', {'error':error,'id':pk})

    return render(request, 'libro/eliminar-autor.html', {'autor':autor})
    


