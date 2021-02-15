from django import forms
from .models import Loja, Pergunta, Alternativa


class LojaForm(forms.ModelForm):
    class Meta:
        model = Loja
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome da Loja'
            })
        }


class PerguntaForm(forms.ModelForm):
    class Meta:
        model = Pergunta
        fields = {'loja', 'pergunta_texto', 'isAtivo'}
        widgets = {
            'loja': forms.Select(attrs={
                'class': 'form-control'
            }),
            'pergunta_texto': forms.Textarea(attrs={
                'class': 'form-control',
                'row': '3'
            }),
            'isAtivo': forms.CheckboxInput(attrs={
                'class': 'form-check-input'
            })
        }


class AlternativaForm(forms.ModelForm):
    class Meta:
        model = Alternativa
        fields = '__all__'
        widgets = {
            'nome_alternativa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a pergunta'
            }),
            'emoji': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cole o emoji'
            })
        }