from django.db import models
from django import forms

# Create your models here.
class Servico(models.Model):
    nome = models.CharField('Nome do serviço', max_length=100)
    descricao = models.TextField('Descrição do Serviço')
    imagem = models.ImageField(upload_to = 'servicos/', default = 'servicos/default.jpg')
    
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

class Contato(models.Model):
    facebook = models.TextField('Pergil no Facebook', default="http://fb.me/MinhaPagina")
    instagram = models.TextField('Instagram', dafault="instagram.com/MinhaPagina")
    email = models.EmailField('Email', default="meuemail@minhaempresa.com")
    telefone = models.CharField(max_length=20, default="(00) 0.0000-0000")
    local = models.TextField('Localização', default="Meu local no mundo")
    gmaps = models.TextField('Link do Google Maps', default="https://goo.gl/maps/gN3aVB8nCzm")

    class Meta:
        verbose_name='Informações de contato'
        verbose_name_plural='Informações de contato'

    def __str__(self):
        return "contato"


