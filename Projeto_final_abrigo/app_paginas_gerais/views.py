from django.shortcuts import render
from django.http import HttpResponse 
from app_animais.models import Animal

def inicial(request):
    animais = Animal.objects.filter(disponivel=True)
    return render(request, 'inicial.html', {'animais': animais})

def sobre(request):
    return render(request, 'sobre.html')

