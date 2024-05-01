from django.shortcuts import render, get_object_or_404
from app_animais.models import Animal
from django.http import JsonResponse
from django.db.models import Q


def animal_list(request):
    animais_disponiveis = Animal.objects.filter(disponivel=True)
    return render(request, 'animais.html', {'animais': animais_disponiveis})

def animal_detail(request, pk):
    animal = get_object_or_404(Animal, pk=pk)
    return render(request, 'animal_detail.html', {'animal': animal})

def animal_filter(request):
    if 'especie' in request.GET:
        especie = request.GET('especie', '')
        animais = Animal.objects.filter(especie_contains=especie)
    else:
        animais = Animal.objects.all()
    contexto = {'animais': animais}
    
    return render(request, 'animais.html', contexto)

def search_animais(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Animal.objects.filter(
            Q(nome__icontains=query) |
            Q(info_animais__icontains=query) |
            Q(especie__especie__icontains=query) |  
            Q(raca__raca__icontains=query) |     
            Q(idade__icontains=query) |           
            Q(porte__porte__icontains=query) |    
            Q(sexo__sexo__icontains=query)       
        )
    return render(request, 'search.html', {'results': results})