# forms.py

from django import forms
from .models import Banner, SecaoEnsino, Projeto, Agendamento

class BannerForm(forms.ModelForm):
    class Meta:
        model = Banner
        fields = ['texto_principal', 'texto_secundario', 'imagem']

class SecaoEnsinoForm(forms.ModelForm):
    class Meta:
        model = SecaoEnsino
        fields = ['titulo', 'descricao', 'imagem']

class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['titulo', 'descricao', 'imagem']

class AgendamentoForm(forms.ModelForm):
    UNIDADE_CHOICES = [
        ('Primavera', 'Unidade Primavera'),
        ('BelaVista', 'Unidade Bela Vista'),
    ]

    unidade = forms.ChoiceField(choices=UNIDADE_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    data = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date', 'class': 'form-control'
    }))
    hora = forms.TimeField(widget=forms.TimeInput(attrs={
        'type': 'time', 'class': 'form-control', 'min': '08:00', 'max': '17:00'
    }))

    class Meta:
        model = Agendamento
        fields = ['nome', 'email', 'telefone', 'unidade', 'data', 'hora']

