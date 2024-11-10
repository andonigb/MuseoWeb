from django.urls import path
from . import views

urlpatterns = [
    path('nombre/', views.mostrar_nombre, name='mostrar_nombre'),
]
