# outra forma de criar urls, criando um arquivo de urls para cada aplicativo a fim de facilitar a organização

from django.urls import path
from app_adotantes.views import cadastrar_adocao, listar_adocao, editar_adocao 

app_name = 'app_adotantes'
urlpatterns = [
    path('', listar_adocao, name='listar_adocao'),
    path('cadastrar', cadastrar_adocao, name='cadastrar_adocao'),
    path('editar/<int:adocao_id>/', editar_adocao, name='editar_adocao'),
]
