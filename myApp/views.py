import os
from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
from django.contrib import messages
from django.conf import settings
from .models import Usuario, Artista

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
    artistas_folder = os.path.join(settings.BASE_DIR, 'myApp/static/imagenes/artistas')
    artistas = []

    for artist in Artista.objects.all():  # Obtén los datos de cada artista desde la base de datos
        artist_folder_path = os.path.join(artistas_folder, artist.nom_artista)  # Usa el nombre del artista para buscar la imagen
        image_path = static(f'imagenes/artistas/{artist.nom_artista}/{artist.nom_artista}.jpg')
        artistas.append({'id_artista': artist.id_artista, 'nombre': artist.nom_artista, 'image_path': image_path})
        print("Ruta generada:", image_path)  # Para verificar la ruta en la consola

    return render(request, 'paginaPrincipal.html', {'artistas': artistas})


def detalle_artista(request, nombre):
    # Obtén el artista desde la base de datos usando el nombre completo
    artista_obj = get_object_or_404(Artista, nom_artista=nombre)

    # Crea un diccionario con los detalles del artista
    artista = {
        "ID": artista_obj.id_artista,
        "Nombre": artista_obj.nom_artista,
        "Nacionalidad": artista_obj.pais_artista,
        "Biografía": artista_obj.biografia,
        "Curiosidades": artista_obj.curiosidades,
    }
    print(artista["Curiosidades"])
    return render(request, 'artista.html', {'artista': artista})





    
