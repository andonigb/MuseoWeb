from django.urls import path
from . import views
from .views import MuseoLoginView

urlpatterns = [
    path('', MuseoLoginView.as_view(), name='login'),
]
