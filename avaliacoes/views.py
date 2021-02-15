from django.shortcuts import render, redirect
from .models import Loja, Pergunta, Alternativa, Voto
from .forms import LojaForm, PerguntaForm, AlternativaForm
from datetime import date
from django.contrib import messages


def listar_lojas(request):
    lojas = Loja.objects.all()
    context = {
        'lojas': lojas
    }
    return render(request, 'pesquisa/index.html', context)


def listar_perguntas(request, id):
    loja = Loja.objects.get(pk=id)
    perguntas = Pergunta.objects.filter(loja_id=loja.id)
    context = {
        'loja': loja,
        'perguntas': perguntas
    }
    return render(request, 'pesquisa/perguntas.html', context)


def listar_alternativas(request, id):
    pergunta = Pergunta.objects.get(pk=id)
    alternativas = Alternativa.objects.filter(pergunta_id=pergunta.id)
    context = {
        'pergunta': pergunta,
        'alternativas': alternativas
    }
    return render(request, 'pesquisa/alternativas.html', context)


def votar(request, id):
    alternativa = Alternativa.objects.get(pk=id)
    voto, created = Voto.objects.get_or_create(alternativa_id=alternativa.id, data_voto=date.today())

    if voto.data_voto == date.today():
        voto.quant_votos += 1
        voto.save()
        messages.success(request, 'Obrigado por colaborar!')
        return redirect('/pesquisa-loja/'+str(alternativa.pergunta_id))

    messages.success(request, 'Obrigado por colaborar!')
    return redirect('/pesquisa-loja/'+str(alternativa.pergunta_id))


# Cadastros

def cadastrar_loja(request):
    lojas = Loja.objects.all()
    if request.method == "GET":
        form = LojaForm()
        context = {
            'lojas': lojas,
            'form': form
        }
        return render(request, 'cadastros/loja_form.html', context)

    elif request.method == "POST":
        form = LojaForm(request.POST)
        if form.is_valid():
            loja = form.save(commit=False)
            form.save()
            messages.success(request, 'Loja cadastrada com Sucesso!')
            return redirect('cadastrar_loja')

        else:
            context = {
                'form': form
            }
            return render(request, 'cadastros/loja_form.html', context)
