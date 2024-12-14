import os
from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
from django.contrib import messages
from django.conf import settings
from .models import Usuario, Artista, Obras, Museo, Epoca, favoritasObras, favoritasArtista, favoritasMuseos
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        try:
            usuario = Usuario.objects.get(usuario=username)
            if check_password(password, usuario.password):
                request.session['usuario_id'] = usuario.id_usuario
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)

                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': True, 'redirect_url': reverse('paginaPrincipal')})

                return redirect('paginaPrincipal')

            else:
                error_message = 'Contraseña incorrecta'
                if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                    return JsonResponse({'success': False, 'errors': [error_message]})
                messages.error(request, error_message)
                return render(request, 'login.html')

        except Usuario.DoesNotExist:
            error_message = 'Usuario no encontrado'
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': [error_message]})
            messages.error(request, error_message)
            return render(request, 'login.html')

    return render(request, 'login.html')

def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if Usuario.objects.filter(usuario=username).exists():
            error_message = 'El nombre de usuario ya está en uso.'
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': [error_message]})
            messages.error(request, error_message)
            return render(request, 'login.html')

        if Usuario.objects.filter(email=email).exists():
            error_message = 'El correo electrónico ya está registrado.'
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': False, 'errors': [error_message]})
            messages.error(request, error_message)
            return render(request, 'login.html')

        password_hashed = make_password(password)
        usuario = Usuario(usuario=username, email=email, password=password_hashed)
        usuario.save()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'redirect_url': reverse('login')})

        messages.success(request, 'Registro exitoso. Ahora puedes iniciar sesión.')
        return redirect('login')

    return render(request, 'login.html')
def principal_view(request):
    
    artistas = []
    museos = []
    movimientos = []
    obras_mas_gustadas=[]

    for artist in Artista.objects.all(): 
        image_path = static(f'imagenes/artistas/{artist.nom_artista}/{artist.nom_artista}.jpg')
        artistas.append({'id_artista': artist.id_artista, 'nombre': artist.nom_artista, 'image_path': image_path})
        
    for museum in Museo.objects.all():
        image_path = static(f'imagenes/museos/{museum.nom_museo}/Logo.jpg')
        museos.append({'id_museo': museum.id_museo, 'nombre': museum.nom_museo, 'image_path': image_path})

    for movement in Epoca.objects.all():
        image_path = static(f'imagenes/movimientos/{movement.nom_epoca}.jpg')
        movimientos.append({'id_epoca': movement.id_epoca, 'nombre': movement.nom_epoca, 'fecha': movement.anyos_epoca, 'image_path': image_path})
        print("RUTA: ",image_path)

    for obra in Obras.objects.order_by('-num_meGustas')[:10]:
        artista=obra.id_artista
        image_path=static(f'imagenes/artistas/{artista.nom_artista}/obras/{obra.nom_obra}.jpg')
        obras_mas_gustadas.append({
            'id_obra':obra.id_obra,
            'nombre': obra.nom_obra,
            'image_path': image_path,
            'num_meGustas': obra.num_meGustas,
        })



    return render(request, 'paginaPrincipal.html', {
        'artistas': artistas,
        'museos': museos,
        'movimientos': movimientos,
        'obras_mas_gustadas':obras_mas_gustadas,
        })


def detalle_artista(request, nombre):
    artista = get_object_or_404(Artista, nom_artista=nombre) 
    obra = []

    for o in Obras.objects.filter(id_artista=artista):
        image_path = static(f'imagenes/artistas/{nombre}/obras/{o.nom_obra}.jpg')
        obra.append({'id_obra': o.id_obra, 'nombre': o.nom_obra, 'image_path': image_path})

    return render(request, 'artista.html', {
        'artista': artista,
        'obra': obra,
    })

def detalle_museo(request, id):
    museo = get_object_or_404(Museo, id_museo=id)
    obra = []

    for o in Obras.objects.filter(id_museo=museo.id_museo):
        artista_instance = get_object_or_404(Artista, id_artista=o.id_artista_id)
        image_path = static(f'imagenes/artistas/{artista_instance.nom_artista}/obras/{o.nom_obra}.jpg')
        obra.append({'id_obra': o.id_obra, 'nombre': o.nom_obra, 'museo': museo.nom_museo, 'image_path': image_path})

    return render(request, 'museo.html', {
        'museo': museo,
        'obra': obra,
    })

def detalle_movimiento(request, id):
    movimiento = get_object_or_404(Epoca, id_epoca=id)
    obra = []
    for o in Obras.objects.filter(id_epoca=movimiento.id_epoca):
        artista_instance = get_object_or_404(Artista, id_artista=o.id_artista_id)
        image_path = static(f'imagenes/artistas/{artista_instance.nom_artista}/obras/{o.nom_obra}.jpg')
        obra.append({'id_obra': o.id_obra, 'nombre': o.nom_obra, 'image_path': image_path})

    return render(request, 'movimiento.html', {
        'movimiento': movimiento,
        'obra': obra,
    })

from django.templatetags.static import static

def detalle_obra(request, id):
    obra_obj = get_object_or_404(Obras, id_obra=id)

    artista_instance = get_object_or_404(Artista, id_artista=obra_obj.id_artista_id)
    museo_instance = get_object_or_404(Museo, id_museo=obra_obj.id_museo_id)
    epoca_instance = get_object_or_404(Epoca, id_epoca=obra_obj.id_epoca_id)

    obra = {
        'id_obra': obra_obj.id_obra,
        'nombre': obra_obj.nom_obra,
        'artista': artista_instance.nom_artista,
        'museo': museo_instance.nom_museo,
        'epoca': epoca_instance.nom_epoca,
        'num_meGustas': obra_obj.num_meGustas,
        'image_path': static(f'imagenes/artistas/{artista_instance.nom_artista}/obras/{obra_obj.nom_obra}.jpg')
    }

    # Comprobar si el usuario ha iniciado sesión y si la obra está en sus favoritos
    usuario_id = request.session.get('usuario_id')
    is_liked = False  # Valor predeterminado
    if usuario_id:
        usuario = get_object_or_404(Usuario, id_usuario=usuario_id)
        # Verificar si la obra está en favoritos
        if favoritasObras.objects.filter(id_usuario=usuario, id_obra=obra_obj).exists():
            is_liked = True

    return render(request, 'obra.html', {
        'obra': obra,
        'is_liked': is_liked,  # Enviar la información de si está en favoritos
    })

def favoritos_view(request):
    usuario_id = request.session.get('usuario_id')
    if not usuario_id:
        return redirect('login')  
    
    try:
        usuario = Usuario.objects.get(id_usuario=usuario_id) 
    except Usuario.DoesNotExist:
        return redirect('login') 

    obras_favoritas = favoritasObras.objects.filter(id_usuario=usuario)
    artistas_favoritas = favoritasArtista.objects.filter(id_usuario=usuario)
    museos_favoritas = favoritasMuseos.objects.filter(id_usuario=usuario)

    obras_favoritas = [fav.id_obra for fav in obras_favoritas]
    artistas_favoritas = [fav.id_artista for fav in artistas_favoritas]
    museos_favoritas = [fav.id_museo for fav in museos_favoritas]

    return render(request, 'favoritos.html', {
        'obras_favoritas': obras_favoritas,
        'artistas_favoritas': artistas_favoritas,
        'museos_favoritas': museos_favoritas,
    })


def artistas_view(request):
    artistas = []
    for artist in Artista.objects.all(): 
        image_path = static(f'imagenes/artistas/{artist.nom_artista}/{artist.nom_artista}.jpg')
        artistas.append({'id_artista': artist.id_artista, 'nombre': artist.nom_artista, 'image_path': image_path})
  
    return render(request, 'artistas.html', {
            'artistas': artistas,
    })

def obras_view(request):
    obras=[]
    for obra in Obras.objects.all():
        artista=obra.id_artista
        image_path=static(f'imagenes/artistas/{artista.nom_artista}/obras/{obra.nom_obra}.jpg')
        obras.append({
            'id_obra':obra.id_obra,
            'nombre': obra.nom_obra,
            'image_path': image_path,
            'num_meGustas': obra.num_meGustas,
        })
    return render(request, 'obras.html', {
        'obras':obras,
    })

def museos_view(request):
    museos = []
    for museum in Museo.objects.all():
        image_path = static(f'imagenes/museos/{museum.nom_museo}/Logo.jpg')
        museos.append({'id_museo': museum.id_museo, 'nombre': museum.nom_museo, 'image_path': image_path})

    return render(request, 'museos.html', {
        'museos': museos,
    })
    

def movimientos_view(request):
    movimientos = []
    for movement in Epoca.objects.all():
        image_path = static(f'imagenes/movimientos/{movement.nom_epoca}.jpg')
        movimientos.append({'id_epoca': movement.id_epoca, 'nombre': movement.nom_epoca, 'fecha': movement.anyos_epoca, 'image_path': image_path})
        print("RUTA: ",image_path)
    return render(request, 'movimientos.html', {
        'movimientos': movimientos,
    })


def search_results(request):
    if request.accepts("application/json"):
        res = None
        obra = request.POST.get('obra')
        print(obra)
        qs = Obras.objects.filter(nom_obra__icontains=obra)
        if len(qs) > 0 and len(obra) > 0:
            data = []
            for pos in qs:
                item = {
                    'nombre': pos.nom_obra,
                    'id_obra': pos.id_obra
                }
                data.append(item)
            res = data
        else:
            res = "No se encontro ninguna obra"
        return JsonResponse({'data': res})

    return JsonResponse({})

def like_obra(request, obra_id):
    if request.method == "POST":
        try:
            # Obtener la obra
            obra = get_object_or_404(Obras, id_obra=obra_id)
            
            # Verificar si el usuario está autenticado
            usuario_id = request.session.get('usuario_id')
            if not usuario_id:
                return JsonResponse({'success': False, 'message': 'Usuario no autenticado'}, status=401)
            
            # Obtener la instancia del usuario
            usuario = get_object_or_404(Usuario, id_usuario=usuario_id)

            # Verificar si la obra ya está en favoritos
            favoritos_entry = favoritasObras.objects.filter(id_usuario=usuario, id_obra=obra).first()

            if favoritos_entry:
                # Si ya está en favoritos, eliminarla (unlike)
                favoritos_entry.delete()
                obra.num_meGustas -= 1
                obra.save()
                is_liked = False  # Indica que ya no está en favoritos
            else:
                # Si no está en favoritos, añadirla (like)
                favoritasObras.objects.create(id_usuario=usuario, id_obra=obra)
                obra.num_meGustas += 1
                obra.save()
                is_liked = True  # Indica que ahora está en favoritos

            # Generar las URLs de los íconos del corazón
            red_heart_url = static('/imagenes/Corazon_Rojo.png')
            default_heart_url = static('/imagenes/Corazon.png')

            return JsonResponse({
                'success': True, 
                'is_liked': is_liked, 
                'num_meGustas': obra.num_meGustas,
                'redHeartUrl': red_heart_url,
                'defaultHeartUrl': default_heart_url
            })
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    return JsonResponse({'success': False, 'message': 'Método no permitido'}, status=405)
     

     


