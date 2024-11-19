# models.py

from django.db import models
from ckeditor.fields import RichTextField

class Banner(models.Model):
    texto_principal = models.CharField(max_length=200, blank=True, null=True)
    texto_secundario = models.CharField(max_length=200, blank=True, null=True)  # Define um valor padrão aqui
    imagem = models.ImageField(upload_to='banners/', blank=True, null=True)

    def __str__(self):
        return f"Banner {self.id}"

class SecaoEnsino(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = RichTextField()
    imagem = models.ImageField(upload_to='secoes/', blank=True, null=True, default='default.jpg')

    def __str__(self):
        return self.titulo

class Projeto(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = RichTextField()
    imagem = models.ImageField(upload_to='projetos/')

    def __str__(self):
        return self.titulo

class Agendamento(models.Model):
    UNIDADE_CHOICES = [
        ('Primavera', 'Unidade Primavera'),
        ('BelaVista', 'Unidade BelaVista'),
    ]
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    data = models.DateField()
    hora = models.TimeField()
    unidade = models.CharField(max_length=20, choices=UNIDADE_CHOICES, default='Primavera')
    status = models.CharField(max_length=50, choices=[('Pendente', 'Pendente'), ('Confirmado', 'Confirmado'), ('Cancelado', 'Cancelado')])

    def __str__(self):
        return f"{self.nome} - {self.data} {self.hora}"
