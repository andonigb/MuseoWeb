from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('Principal/', views.paginaPrincipal, name='paginaPrincipal'),

]
