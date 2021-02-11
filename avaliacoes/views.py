from django.shortcuts import render, redirect
from .models import Loja, Alternativa, Voto
from datetime import date


def listar_lojas(request):
    lojas = Loja.objects.all()
    context = {
        'lojas': lojas
    }
    return render(request, 'index.html', context)


def listar_alternativas(request, id):
    loja = Loja.objects.get(pk=id)
    alternativas = Alternativa.objects.filter(loja=loja.id)
    context = {
        'loja': loja,
        'alternativas': alternativas
    }
    return render(request, 'alternativas.html', context)


def votar(request, id):
    alternativa = Alternativa.objects.get(pk=id)
    voto, created = Voto.objects.get_or_create(alternativa_id=alternativa.id, data_voto=date.today())

    if voto.data_voto == date.today():
        voto.quant_votos += 1
        voto.save()
        return redirect('listar_lojas')

    return redirect('listar_lojas')


# if created:
#     voto.alternativa = alternativa
#     voto.quant_votos = 1
#     voto.save()
#     return redirect('listar_lojas')


# Indo Certo
# def votar(request, id):
#     alternativa = Alternativa.objects.get(pk=id)
#     voto, created = Voto.objects.get_or_create(
#         alternativa_id=alternativa.id,
#         quant_votos=1
#     )
#
#     if voto.quant_votos == 1:
#         if voto.data_voto == date.today():
#             voto.quant_votos += 1
#             voto.save()
#         return redirect('listar_lojas')
#
#     return redirect('listar_lojas')

# def votar(request, id):
#     alternativa = Alternativa.objects.get(pk=id)
#     v = 0
#
#     voto, created = Voto.objects.get_or_create(
#         alternativa_id=alternativa.id,
#         quant_votos=v
#     )
#
#     if voto.alternativa_id == alternativa.id:
#         if voto.data_voto == date.today():
#             voto.quant_votos += 1
#             voto.save()
#     return redirect('listar_lojas')
