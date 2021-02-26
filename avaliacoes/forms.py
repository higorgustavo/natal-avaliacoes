from django import forms
from .models import Estabelecimento, Enquente, Alternativa


class EstabelecimentoForm(forms.ModelForm):
    class Meta:
        model = Estabelecimento
        fields = '__all__'
        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nome do Estabelecimento'
            })
        }


class EnqueteForm(forms.ModelForm):
    class Meta:
        model = Enquente
        fields = '__all__'
        widgets = {
            'estabelecimento': forms.Select(attrs={
                'class': 'form-control'
            }),
            'enquete_texto': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': '3'
            }),
        }


class AlternativaForm(forms.ModelForm):
    class Meta:
        model = Alternativa
        fields = '__all__'
        widgets = {
            'nome_alternativa': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite a alternativa'
            }),
            'emoji': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Cole o emoji da alternativa'
            })
        }