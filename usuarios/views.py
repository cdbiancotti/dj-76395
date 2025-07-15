from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from django.contrib.auth import login as django_login
from usuarios.forms import FormularioRegistro, FormularioEdicionPerfil
from usuarios.models import InfoExtra

def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            user = formulario.get_user()
            
            django_login(request, user)
            
            InfoExtra.objects.get_or_create(user=user)
            
            return redirect('inicio:inicio')
    else:
        formulario = AuthenticationForm()
    
    return render(request, 'usuarios/login.html', {'formulario': formulario})

def registro(request):
    
    if request.method == 'POST':
        # formulario = UserCreationForm(request.POST)
        formulario = FormularioRegistro(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
    else:
        # formulario = UserCreationForm()
        formulario = FormularioRegistro()
    return render(request, 'usuarios/registro.html', {'formulario': formulario})

def editar_perfil(request):
    
    info_extra = request.user.infoextra
    
    if request.method == 'POST':
        formulario = FormularioEdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            
            avatar_nuevo = formulario.cleaned_data.get('avatar')
            info_extra.avatar = avatar_nuevo
            info_extra.save()
            
            formulario.save()
            return redirect('inicio:inicio')
    else:
        formulario = FormularioEdicionPerfil(instance=request.user, initial={'avatar': info_extra.avatar})
    return render(request, 'usuarios/editar_perfil.html', {'formulario': formulario})