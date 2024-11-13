from django.contrib.auth.hashers import make_password
from myApp.models import Usuario

# Obtener todos los usuarios
usuarios = Usuario.objects.all()

# Iterar sobre cada usuario y cifrar su contraseña
for usuario in usuarios:
    # Si la contraseña no está cifrada (en texto plano), la ciframos
    if not usuario.password.startswith(('pbkdf2_sha256$', 'bcrypt', 'argon2')):
        usuario.password = make_password(usuario.password)
        usuario.save()

print("Contraseñas cifradas correctamente.")
