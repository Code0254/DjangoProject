from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm # Django way (Class) of creating the registration form 

# Create your views here.
def register (request):
    form = UserCreationForm
    return render (request, 'users/register.html', {'form': form}) # request, template, form

