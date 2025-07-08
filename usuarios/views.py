from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as django_login

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            
            django_login(request, user)
            return redirect('inicio:inicio')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})