import django_filters
from django import forms
from .models import *


OPCOES = (
    (True, 'Sim'),
    (False, 'Não'),
)


class PerguntaFilter(django_filters.FilterSet):
    isAtivo = django_filters.ChoiceFilter(choices=OPCOES)

    class Meta:
        model = Pergunta
        fields = ['loja', 'isAtivo']
        # se quiser fazer virar o check
        # filter_overrides = {
        #     models.BooleanField: {
        #         'filter_class': django_filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxInput,
        #         },
        #     },
        # }


