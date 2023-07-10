from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Empresa, Estacionamiento, Estado
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache


def servicios(request):
    return render(request, 'servicios.html')

def contactanos(request):
    return render(request, 'contactanos.html')

def nosotros(request):
    return render(request, 'nosotros.html')


    
def lista_estacionamientos(request):
    estacionamientos = Estacionamiento.objects.all()
    return render(request, 'into.html', {'estacionamientos': estacionamientos})

def estados_estacionamiento(request, estacionamiento_id):
    estacionamiento = Estacionamiento.objects.get(id=estacionamiento_id)
    estados = Estado.objects.filter(id_estacionamiento=estacionamiento)
    return render(request, 'Estados.html', {'estacionamiento': estacionamiento, 'estados': estados})

def empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'empresas.html', {'empresas': empresas})

def login_view(request):
    if request.method == 'POST':
        correo = request.POST['username']
        clave = request.POST['password']

        try:
            empresa = Empresa.objects.get(correo=correo)
            if empresa.clave == clave:
                estacionamientos = Estacionamiento.objects.all()
                return lista_estacionamientos(request)
            else:
                # La clave es incorrecta, mostrar un mensaje de error
                messages.error(request, 'La clave ingresada es incorrecta.')
        except Empresa.DoesNotExist:
            # No se encontró ninguna empresa con el correo ingresado, mostrar un mensaje de error
            messages.error(request, 'No existe una cuenta asociada a ese correo.')

    # Si el usuario ya ha iniciado sesión y trata de acceder a la página de inicio de sesión, redirigirlo a la página de inicio
    if request.user.is_authenticated:
        return redirect('smartparking:home')

    return render(request, 'login.html')

@login_required(login_url='smartparking:login')
def into(request):
    return render(request, 'into.html')

@never_cache
def logout_view(request):
    logout(request)
    return redirect('smartparking:login')

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
