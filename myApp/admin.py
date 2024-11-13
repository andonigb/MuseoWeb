from django.contrib import admin
from .models import Usuario, Artista, Obras, Epoca, Museo  # Asegúrate de importar tus modelos

admin.site.register(Usuario)
admin.site.register(Artista)
admin.site.register(Obras)
admin.site.register(Epoca)
admin.site.register(Museo)

