from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.

def signup(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = UserCreationForm()
    context={
        'form':form
    }
    return render(request,'accounts/forms.html',context)

def login(request):
    if request.user.is_authenticated:
        return redirect('movies:index')

    if request.method == "POST":
        form = AuthenticationForm(request,request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'accounts/forms.html',context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

