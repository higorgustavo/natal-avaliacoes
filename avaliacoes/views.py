from django.shortcuts import render, redirect
from .models import Estabelecimento, Enquente, Alternativa, Voto
from .forms import EstabelecimentoForm, EnqueteForm, AlternativaForm
from django.forms import inlineformset_factory
from datetime import date
from django.contrib import messages
from .filters import EnqueteFilter


def listar_estabeleciomentos(request):
    estabeleciomentos = Estabelecimento.objects.all()
    context = {
        'estabeleciomentos': estabeleciomentos
    }
    return render(request, 'pesquisa/index.html', context)


def listar_enquetes(request, id):
    estabelecimento = Estabelecimento.objects.get(pk=id)
    enquetes = Enquente.objects.filter(estabelecimento_id=estabelecimento.id, isAtiva=True)
    context = {
        'estabelecimento': estabelecimento,
        'enquetes': enquetes
    }
    return render(request, 'pesquisa/enquetes.html', context)


def listar_alternativas(request, id):
    enquete = Enquente.objects.get(pk=id)
    alternativas = Alternativa.objects.filter(enquete_id=enquete.id)
    context = {
        'enquete': enquete,
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
        return redirect('/enquete/' + str(alternativa.enquete_id) + '/alternativas')

    messages.success(request, 'Obrigado por colaborar!')
    return redirect('/enquete/' + str(alternativa.enquete_id) + '/alternativas')


# Cadastros
def cadastrar_estabelecimento(request):
    estabelecimentos = Estabelecimento.objects.all()
    if request.method == "GET":
        form = EstabelecimentoForm()
        context = {
            'estabelecimentos': estabelecimentos,
            'form': form
        }
        return render(request, 'estabelecimento/estabelecimento_form.html', context)

    elif request.method == "POST":
        form = EstabelecimentoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estabelecimento cadastrado com Sucesso!')
            return redirect('cadastrar_estabelecimento')

        else:
            context = {
                'form': form
            }
            return render(request, 'estabelecimento/estabelecimento_form.html', context)


def editar_estabelecimento(request, id):
    estabelecimento = Estabelecimento.objects.get(pk=id)
    form = EstabelecimentoForm(instance=estabelecimento)
    if request.method == "POST":
        form = EstabelecimentoForm(request.POST, instance=estabelecimento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Estabelecimento atualizado com sucesso!')
            return redirect('cadastrar_estabelecimento')

    context = {
        'form': form
    }
    return render(request, 'estabelecimento/edit_estabelecimento.html', context)


def deletar_estabelecimento(request, id):
    estabelecimento = Estabelecimento.objects.get(pk=id)
    if request.method == "POST":
        estabelecimento.delete()
        messages.success(request, 'Estabelecimento deletado com sucesso!')
        return redirect('cadastrar_estabelecimento')

    context = {
        'estabelecimento': estabelecimento
    }
    return render(request, 'estabelecimento/delete_estabelecimento.html', context)


# Perguntas e Alternativas
def gerenciar_lista_esquentes(request):
    enquetes = Enquente.objects.all()
    enquete_filter = EnqueteFilter(request.GET, queryset=enquetes)
    enquetes = enquete_filter.qs
    context = {
        'enquetes': enquetes,
        'enquete_filter': enquete_filter
    }
    return render(request, 'enquete/list_enquetes.html', context)


def cadastrar_enquete(request):
    if request.method == "GET":
        form_e = EnqueteForm()
        form_alternativa_factory = inlineformset_factory(Enquente, Alternativa, form=AlternativaForm, extra=1)
        form_a = form_alternativa_factory()

        context = {
            'form_e': form_e,
            'form_a': form_a,
        }
        return render(request, 'enquete/create_enquete.html', context)

    elif request.method == "POST":
        form_e = EnqueteForm(request.POST or None)
        form_alternativa_factory = inlineformset_factory(Enquente, Alternativa, form=AlternativaForm)
        form_a = form_alternativa_factory(request.POST or None)

        if form_e.is_valid() and form_a.is_valid():
            enquete = form_e.save()
            form_a.instance = enquete
            form_a.save()
            messages.success(request, 'Enquete cadastrada com sucesso!')
            return redirect('gerenciar_lista_esquentes')

        else:
            context = {
                'form_e': form_e,
                'form_a': form_a,
            }
            return render(request, 'enquete/create_enquete.html', context)


def editar_enquete(request, id):
    if request.method == "GET":
        enquete = Enquente.objects.get(pk=id)
        if enquete is None:
            return redirect('gerenciar_lista_esquentes')
        form_e = EnqueteForm(instance=enquete)

        form_alternativa_factory = inlineformset_factory(Enquente, Alternativa, form=AlternativaForm, extra=0)
        form_a = form_alternativa_factory(instance=enquete)

        context = {
            'enquete': enquete,
            'form_e': form_e,
            'form_a': form_a,
        }
        return render(request, 'enquete/edit_enquete.html', context)

    elif request.method == "POST":
        enquete = Enquente.objects.get(pk=id)
        if enquete is None:
            return redirect('gerenciar_lista_esquentes')
        form_e = EnqueteForm(request.POST or None, instance=enquete)

        form_alternativa_factory = inlineformset_factory(Enquente, Alternativa, form=AlternativaForm)
        form_a = form_alternativa_factory(request.POST or None, instance=enquete)

        if form_e.is_valid() and form_a.is_valid():
            enquete_atualizada = form_e.save()
            form_a.instance = enquete_atualizada
            form_a.save()

            messages.success(request, 'Enquete atualizada com sucesso!')
            return redirect('gerenciar_lista_esquentes')

        context = {
            'enquete': enquete,
            'form_e': form_e,
            'form_a': form_a,
        }
        return render(request, 'enquete/edit_enquete.html', context)


def deletar_enquete(request, id):
    enquete = Enquente.objects.get(pk=id)
    if request.method == "POST":
        enquete.delete()
        messages.success(request, 'Enquete excluída com sucesso!')
        return redirect('gerenciar_lista_esquentes')

    context = {
        'enquete': enquete
    }
    return render(request, 'enquete/delete_enquete.html', context)


# Resultados
def resultados(request):
    enquetes = Enquente.objects.all().filter(isAtiva=True)
    enquete_filter = EnqueteFilter(request.GET, queryset=enquetes)
    enquetes = enquete_filter.qs
    context = {
        'enquetes': enquetes,
        'enquete_filter': enquete_filter
    }
    return render(request, 'resultado/list_resultados.html', context)


def resultado_enquete(request, id):
    enquete = Enquente.objects.get(pk=id)
    alternativas = Alternativa.objects.filter(enquete_id=enquete.id)
    context = {
        'enquete': enquete,
        'alternativas': alternativas
    }
    return render(request, 'resultado/resultado_enquete.html', context)