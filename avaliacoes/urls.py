from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_estabeleciomentos, name='listar_estabeleciomentos'),
    path('estabelecimento/<int:id>/enquetes', listar_enquetes, name='listar_enquetes'),
    path('enquete/<int:id>/alternativas', listar_alternativas, name='listar_alternativas'),
    path('voto/<int:id>/', votar, name='votar'),

    # CRUD
    path('estabelecimentos/', cadastrar_estabelecimento, name='cadastrar_estabelecimento'),
    path('estabelecimento/<int:id>/editar', editar_estabelecimento, name='editar_estabelecimento'),
    path('estabelecimento/<int:id>/deletar', deletar_estabelecimento, name='deletar_estabelecimento'),
    path('enquetes/', gerenciar_lista_esquentes, name='gerenciar_lista_esquentes'),
    path('enquete/add', cadastrar_enquete, name='cadastrar_enquete'),
    path('enquete/<int:id>/editar', editar_enquete, name='editar_enquete'),
    path('enquete/<int:id>/deletar', deletar_enquete, name='deletar_enquete'),

    # Resultados
    path('resultados/', resultados, name='resultados'),
    path('enquete/<int:id>/resultado', resultado_enquete, name='resultado_enquete'),
]
