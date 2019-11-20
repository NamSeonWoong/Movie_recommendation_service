from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == "POST":
        pass
    else:
        form = UserCreationForm()
    context={
        'form':form
    }
    

def login(request):
    pass

def logout(request):
    pass

def userlist(request):
    pass
