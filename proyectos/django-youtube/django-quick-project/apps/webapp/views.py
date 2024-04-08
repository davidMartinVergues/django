from django.shortcuts import render,redirect
from django.http import HttpResponse

from .forms import CreateUserForm, LoginForm


def home(request):
    # return HttpResponse('Hello world')
    return render(request,'webapp/index.html')

# - Register a user

def register(request):
    
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save() # sending data from form 

            #return redirect('')

    
    context = {"form":form}

    return render(request,'webapp/register.html',context=context)
    

