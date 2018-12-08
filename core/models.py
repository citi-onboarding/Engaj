from django.db import models
from django import forms

# Create your models here.

class Banner(models.Model):
    frase = models.CharField('Frase para o banner inicial', max_length=30)

    def __str__(self):
        return self.frase

class Servico(models.Model):
    nome = models.CharField('Nome do serviço', max_length=100)
    descricao = models.TextField('Descrição do Serviço')
    imagem = models.ImageField(upload_to = 'servicos/', default = 'servicos/default.png')
    
    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.nome

# Ver como tornar único  
class Sobre(models.Model):
    descricao = models.TextField('Descrição da Engaj')
    imagem = models.ImageField(upload_to = 'sobre/', default = 'sobre/default.jpg')
    visao = models.TextField('Visão da Engaj')
    missao = models.TextField('Missao da Engaj')

    class Meta:
        verbose_name = 'Sobre'   
        verbose_name_plural = 'Sobre'   

    def __str__(self):
        return "Sobre a Engaj"

class Valor(models.Model):
    descricao = models.TextField('Valor da Engaj')
    
    class Meta:
        verbose_name = 'Valor'   
        verbose_name_plural = 'Valores'   

    def __str__(self):
        return self.descricao
