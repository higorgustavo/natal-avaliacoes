from django.shortcuts import render, redirect
from .models import Loja, Avaliacao
from datetime import date


def listar_lojas(request):
    lojas = Loja.objects.all()
    context = {
        'lojas': lojas
    }
    return render(request, 'index.html', context)


def opcoes_avaliacao(request, id):
    loja = Loja.objects.get(pk=id)
    avaliacoes = Avaliacao.objects.filter(loja_id=loja.id)
    context = {
        'loja': loja,
        'avaliacoes': avaliacoes
    }
    return render(request, 'opcoes.html', context)


def votar(request, id):
    avaliacao = Avaliacao.objects.get(pk=id)
    avaliacao.quant_votos += 1
    avaliacao.save()
    return redirect('listar_lojas')