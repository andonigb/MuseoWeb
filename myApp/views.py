# views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Usuario
from django.contrib.auth.hashers import check_password  # Usamos esto para verificar contraseñas
from django.shortcuts import render, redirect
from .models import Usuario

def login_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        username = request.POST['username']
        password = request.POST['password']

        try:
            # Buscar el usuario en la base de datos
            usuario = Usuario.objects.get(usuario=username)

            # Comparar la contraseña ingresada con la almacenada en la base de datos
            if usuario.password == password:
                # Iniciar sesión (esto es solo un ejemplo, necesitarás gestionarlo de forma adecuada)
                request.session['usuario_id'] = usuario.id_usuario
                return redirect('paginaPrincipal')  # Redirigir a la página principal

            else:
                # Si la contraseña no es correcta
                error = 'Contraseña incorrecta'
                return render(request, 'login.html', {'error': error})
        
        except Usuario.DoesNotExist:
            # Si el usuario no existe
            error = 'Usuario no encontrado'
            return render(request, 'login.html', {'error': error})

    return render(request, 'login.html')

def paginaPrincipal(request):
    return render(request, 'paginaPrincipal.html')


    
