# default django form to create users
from django.contrib.auth.forms import UserCreationForm
# para crear form para authentication
from django.contrib.auth.forms import AuthenticationForm
# user model by default 
from django.contrib.auth.models import User

# para poder usar los tipos de cada field, por ejmplo txt, number, password...
from django import forms

# este input permite importar los widgets, password input widgets and text import widget
from django.forms.widgets import PasswordInput,TextInput

# Create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','password1','password2']


# login a user
class  LoginForm(AuthenticationForm):

    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())