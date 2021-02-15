from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_lojas, name='listar_lojas'),
    path('perguntas/<int:id>/', listar_perguntas, name='listar_perguntas'),
    path('pesquisa-loja/<int:id>/', listar_alternativas, name='listar_alternativas'),
    path('voto/<int:id>/', votar, name='votar'),

    # CRUD
    path('loja/', cadastrar_loja, name='cadastrar_loja'),
]
