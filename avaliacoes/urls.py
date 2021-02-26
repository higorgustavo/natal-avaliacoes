from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_estabeleciomentos, name='listar_estabeleciomentos'),
    path('estabeleciomento/<int:id>/enquetes', listar_enquetes, name='listar_enquetes'),
    path('enquete/<int:id>/alternativas', listar_alternativas, name='listar_alternativas'),
    path('voto/<int:id>/', votar, name='votar'),

    # CRUD
    path('estabeleciomentos/', cadastrar_estabelecimento, name='cadastrar_estabelecimento'),
    path('estabeleciomento/<int:id>/editar', editar_estabelecimento, name='editar_estabelecimento'),
    path('estabeleciomento/<int:id>/deletar', deletar_estabelecimento, name='deletar_estabelecimento'),
    path('enquetes/', gerenciar_lista_esquentes, name='gerenciar_lista_esquentes'),
    path('enquete/add', cadastrar_enquete, name='cadastrar_enquete'),
    path('enquete/<int:id>/editar', editar_enquete, name='editar_enquete'),
    path('enquete/<int:id>/deletar', deletar_enquete, name='deletar_enquete'),
]
