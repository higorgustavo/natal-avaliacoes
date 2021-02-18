from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_lojas, name='listar_lojas'),
    path('loja/<int:id>/perguntas', listar_perguntas, name='listar_perguntas'),
    path('pergunta/<int:id>/alternativas', listar_alternativas, name='listar_alternativas'),
    path('voto/<int:id>/', votar, name='votar'),

    # CRUD
    path('loja/', cadastrar_loja, name='cadastrar_loja'),
    path('pergunta/', cadastrar_pergunta, name='cadastrar_pergunta'),
]
