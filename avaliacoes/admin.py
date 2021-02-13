from django.contrib import admin
from .models import Loja, Pergunta, Alternativa, Voto


admin.site.register(Loja)
admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Voto)
