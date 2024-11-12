from django.contrib.auth.hashers import make_password
from django.contrib.auth import login
from .models import Usuario
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        
        return redirect('paginaPrincipal')  
    return render(request, 'login.html')

def paginaPrincipal(request):
    return render(request, 'paginaPrincipal.html')

    
