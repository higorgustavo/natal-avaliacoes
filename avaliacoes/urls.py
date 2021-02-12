from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_lojas, name='listar_lojas'),
    path('pesquisa-loja/<int:id>/', listar_alternativas, name='listar_alternativas'),
    path('voto/<int:id>/', votar, name='votar')
]
