from django.shortcuts import render, redirect
from .models import Loja, Alternativa, Voto
from datetime import date


def listar_lojas(request):
    lojas = Loja.objects.all()
    context = {
        'lojas': lojas
    }
    return render(request, 'index.html', context)


def opcoes_avaliacao(request, id):
    loja = Loja.objects.get(pk=id)
    alternativas = Alternativa.objects.filter(loja=loja.id)
    context = {
        'loja': loja,
        'alternativas': alternativas
    }
    return render(request, 'alternativas.html', context)


def votar(request, id):
    pass


# def votar(request, id):
#     avaliacao = Avaliacao.objects.get(pk=id)
#     if avaliacao.data_avaliacao != date.today():
#         new_avaliacao, created = Avaliacao.objects.get_or_create(
#             avaliacao_cliente=avaliacao.avaliacao_cliente,
#             loja_id=avaliacao.loja_id,
#             quant_votos=1
#         )
#         new_avaliacao.save()
#         return redirect('listar_lojas')
#     else:
#         avaliacao.quant_votos += 1
#         avaliacao.save()
#         return redirect('listar_lojas')