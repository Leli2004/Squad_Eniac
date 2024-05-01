from django.contrib import admin
from app_animais.models import Animal, Historico_medico,Raca,Porte,Especie,Sexo

# Register your models here.
@admin.register(Raca)
class RacaAdmin(admin.ModelAdmin):
    list_display = ['raca']
    search_fields = ['raca']
    

@admin.register(Porte)
class PorteAdmin(admin.ModelAdmin):
    list_display = ['porte']
    search_fields = ['porte']
    

@admin.register(Especie)
class EspecieAdmin(admin.ModelAdmin):
    list_display = ['especie']
    search_fields = ['especie']
    

@admin.register(Sexo)
class SexoAdmin(admin.ModelAdmin):
    list_display = ['sexo']
    search_fields = ['sexo']
    

@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome', 'especie', 'raca')
    search_fields = ['nome', 'especie', 'raca', 'porte', 'sexo', 'cachorro', 'gato' ]
    list_filter = ['data']

@admin.register(Historico_medico)
class HistoricoAdmin(admin.ModelAdmin):
    list_display = ('animal', 'data')
    search_fields = ['nome', 'especie', 'raca', 'porte', 'sexo', 'data' ]
    list_filter = ['data']