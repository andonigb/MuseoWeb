import os
from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
from django.contrib import messages
from django.conf import settings
from .models import Usuario, Artista, Obras, Museo

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
    
    artistas = []

    for artist in Artista.objects.all():  # Obtén los datos de cada artista desde la base de datos
        image_path = static(f'imagenes/artistas/{artist.nom_artista}/{artist.nom_artista}.jpg')
        artistas.append({'id_artista': artist.id_artista, 'nombre': artist.nom_artista, 'image_path': image_path})

    return render(request, 'paginaPrincipal.html', {'artistas': artistas})


def detalle_artista(request, nombre):
    # Obtén el artista desde la base de datos usando el nombre completo
    artista_obj = get_object_or_404(Artista, nom_artista=nombre) 
    # Obtén las obras del artista
    obras = Obras.objects.filter(id_artista=artista_obj)
    obra = []
    for o in obras:
        image_path = static(f'imagenes/artistas/{artista_obj.nom_artista}/obras/{o.nom_obra}.jpg')
        obra.append({'image_path': image_path})

    return render(request, 'artista.html', {
        'artista': artista_obj,
        'obras': obras,
        'obra': obra, 
    })

def detalle_obra(request, nombre):
    obra = get_object_or_404(Obras, nom_obra=nombre, artista=artista_instance)
    artista_instance = get_object_or_404(Artista, id_artista = obra.id_artista)
    image_path = static(f'imagenes/artistas/{artista_instance.nom_artista}/obras/{nombre}.jpg')
    path = [{'image_path': image_path}]

    return render(request, 'obra.html', {
        'obra': obra,
        'path': path,
    })



    
