from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_lojas, name='listar_lojas'),
    path('votacao/<int:id>/', opcoes_avaliacao, name='opcoes_avaliacao'),
    path('voto/<int:id>/', votar, name='votar')
]
