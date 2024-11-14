from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('Principal/', views.principal_view, name='paginaPrincipal'),
    path('artista/<str:nombre>/', views.detalle_artista, name='detalle_artista'),

]
