from django.shortcuts import render
from django.http import HttpResponse

def mostrar_nombre(request):
    return HttpResponse('Vincent Van Gogh')

