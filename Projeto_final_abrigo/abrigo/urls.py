"""
URL configuration for abrigo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_adotantes.views import formulario_animal
from django.conf import settings
from django.conf.urls.static import static
from app_paginas_gerais.views import inicial, sobre
from app_animais.views import animal_list, animal_detail
from app_voluntarios.views import voluntarios
from django.urls import path
from app_animais.views import search_animais

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicial, name='inicial'),
    path('sobre/', sobre, name='sobre'),
    path('animal/<int:pk>/formulario', formulario_animal, name='formulario_animal'),
    path('animais/', animal_list, name='animais'),
    path('animais/<int:pk>/', animal_detail, name='animal_detail'),
    path('voluntarios/', voluntarios, name='voluntarios' ),
    path('search/', search_animais, name='search'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )+ [
    # Definindo o caminho para servir arquivos estáticos durante o desenvolvimento
    # Isso serve arquivos estáticos em STATIC_URL (ex: '/static/') para STATIC_ROOT (ex: 'static/')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
