# museo/urls.py
from django.contrib import admin
from django.urls import path, include
from myApp import views  # Importa las vistas de la aplicación 'miapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myApp.urls')), #myApp
]





