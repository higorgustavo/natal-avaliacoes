from django.urls import path
from .views import *

urlpatterns = [
    path('', listar_lojas, name="listar_lojas"),
]
