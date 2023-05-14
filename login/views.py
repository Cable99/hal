from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterUserForm

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'home.html', {}) #reinderizzamento pagina contenete le app
        else:
            messages.success(request, ("C'è stato un errore durante l'autenticazione, riprova"))
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        print(form.errors)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Registrazione avvenuta con successo"))
            return render(request, 'home.html', {}) #reinderizzamento pagina contenete le app
    else:
        form = RegisterUserForm()

    return render(request, 'register.html', {
        'form':form,
    })

def home(request):
    if  request.user.is_authenticated:
        return render(request, 'home.html', {})
    else:
        return redirect('login_user')

def logout_user(request):
    logout(request)
    messages.success(request, ("Log out effettuato"))
    return redirect('login_user')

