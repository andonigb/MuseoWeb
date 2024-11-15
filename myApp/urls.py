from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('Principal/', views.principal_view, name='paginaPrincipal'),
    path('artista/<str:nombre>/', views.detalle_artista, name='detalle_artista'),
    path('museo/<int:id>/', views.detalle_museo, name='detalle_museo'),
    path('movimiento/<int:id>/', views.detalle_movimiento, name='detalle_movimiento'),
    path('obra/<int:id>/', views.detalle_obra, name='detalle_obra'),
]
