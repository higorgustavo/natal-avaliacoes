from django.shortcuts import render, redirect
from .models import Loja, Pergunta, Alternativa, Voto
from .forms import LojaForm, PerguntaForm, AlternativaForm
from django.forms import inlineformset_factory
from datetime import date
from django.contrib import messages
from .filters import PerguntaFilter


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
        return redirect('/pergunta/' + str(alternativa.pergunta_id) + '/alternativas')

    messages.success(request, 'Obrigado por colaborar!')
    return redirect('/pergunta/' + str(alternativa.pergunta_id) + '/alternativas')


# Cadastros
def cadastrar_loja(request):
    lojas = Loja.objects.all()
    if request.method == "GET":
        form = LojaForm()
        context = {
            'lojas': lojas,
            'form': form
        }
        return render(request, 'loja/loja_form.html', context)

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
            return render(request, 'loja/loja_form.html', context)


# Perguntas e Alternativas
def listar_perguntas_gerenciar(request):
    perguntas = Pergunta.objects.all()
    pergunta_filter = PerguntaFilter(request.GET, queryset=perguntas)
    perguntas = pergunta_filter.qs
    context = {
        'perguntas': perguntas,
        'pergunta_filter': pergunta_filter
    }
    return render(request, 'pergunta/list_perguntas.html', context)


def cadastrar_pergunta(request):
    if request.method == "GET":
        form_p = PerguntaForm()
        form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm, extra=1)
        form_a = form_alternativa_factory()

        context = {
            'form_p': form_p,
            'form_a': form_a,
        }
        return render(request, 'pergunta/create_pergunta.html', context)

    elif request.method == "POST":
        form_p = PerguntaForm(request.POST or None)
        form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm)
        form_a = form_alternativa_factory(request.POST or None)

        if form_p.is_valid() and form_a.is_valid():
            pergunta = form_p.save()
            form_a.instance = pergunta
            form_a.save()
            messages.success(request, 'Pergunta cadastrada com sucesso!')
            return redirect('listar_perguntas_gerenciar')

        else:
            context = {
                'form_p': form_p,
                'form_a': form_a,
            }
            return render(request, 'pergunta/create_pergunta.html', context)


def editar_pergunta(request, id):
    if request.method == "GET":
        pergunta = Pergunta.objects.get(pk=id)
        if pergunta is None:
            return redirect('listar_lojas')
        form_p = PerguntaForm(instance=pergunta)

        form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm, extra=0)
        form_a = form_alternativa_factory(instance=pergunta)

        context = {
            'pergunta': pergunta,
            'form_p': form_p,
            'form_a': form_a,
        }
        return render(request, 'pergunta/edit_pergunta.html', context)

    elif request.method == "POST":
        pergunta = Pergunta.objects.get(pk=id)
        if pergunta is None:
            return redirect('listar_perguntas_gerenciar')
        form_p = PerguntaForm(request.POST or None, instance=pergunta)

        form_alternativa_factory = inlineformset_factory(Pergunta, Alternativa, form=AlternativaForm)
        form_a = form_alternativa_factory(request.POST or None, instance=pergunta)

        if form_p.is_valid() and form_a.is_valid():
            pergunta_atualizada = form_p.save()
            form_a.instance = pergunta_atualizada
            form_a.save()

            messages.success(request, 'Pergunta atualizada com sucesso!')
            return redirect('listar_perguntas_gerenciar')

        context = {
            'pergunta': pergunta,
            'form_p': form_p,
            'form_a': form_a,
        }
        return render(request, 'pergunta/edit_pergunta.html', context)


def deletar_pergunta(request, id):
    pergunta = Pergunta.objects.get(pk=id)
    if request.method == "POST":
        pergunta.delete()
        messages.success(request, 'Pergunta excluída com sucesso!')
        return redirect('listar_perguntas_gerenciar')

    context = {
        'pergunta': pergunta
    }
    return render(request, 'pergunta/delete_pergunta.html', context)