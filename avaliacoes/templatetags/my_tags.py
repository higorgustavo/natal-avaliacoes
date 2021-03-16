from django import template
from avaliacoes.models import Voto

register = template.Library()


@register.filter(name="total_votos")
def total_votos(value):
    votos = Voto.objects.filter(alternativa__enquete=value)
    total = sum(votos.values_list('quant_votos', flat=True))
    return total


@register.filter(name="total_votos_alternativa")
def total_votos_alternativa(value):
    votos = Voto.objects.filter(alternativa_id=value)
    total = sum(votos.values_list('quant_votos', flat=True))
    return total


