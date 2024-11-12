from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.views import LoginView

class MuseoLoginView(LoginView):
    template_name = 'login.html'
