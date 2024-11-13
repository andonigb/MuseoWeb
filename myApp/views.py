import os
from django.shortcuts import render, redirect
from django.templatetags.static import static
from django.contrib import messages
from django.conf import settings
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

def principal_view(request):
    print("Pasa")
    artistas_folder = os.path.join(settings.BASE_DIR, 'myApp/static/imagenes/artistas')
    artistas = []
    for folder_name in os.listdir(artistas_folder):
        artist_folder_path = os.path.join(artistas_folder, folder_name)
        if os.path.isdir(artist_folder_path):
            image_path = static(f'imagenes/artistas/{folder_name}/{folder_name}.jpg')
            artistas.append({'nombre': folder_name, 'image_path': image_path})
            print("Ruta generada:", image_path)  # Para verificar la ruta en la consola

    return render(request, 'paginaPrincipal.html', {'artistas': artistas})



    
