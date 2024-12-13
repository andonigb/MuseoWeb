from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('register/', views.register_view, name='registro'),
    path('Principal/', views.principal_view, name='paginaPrincipal'),
    path('artista/<str:nombre>/', views.detalle_artista, name='detalle_artista'),
    path('museo/<int:id>/', views.detalle_museo, name='detalle_museo'),
    path('movimiento/<int:id>/', views.detalle_movimiento, name='detalle_movimiento'),
    path('obra/<int:id>/', views.detalle_obra, name='detalle_obra'),
    path('favoritos/', views.favoritos_view, name='favoritos'),

    path('artistas/', views.artistas_view, name='artistas'),
    path('obras/', views.obras_view, name='obras'),
    path('museos/', views.museos_view, name='museos'),
    path('movimientos/', views.movimientos_view, name='movimientos'),

    path('search/', views.search_results, name='search'),
]
