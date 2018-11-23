from django.db import models

# Create your models here.
class Servico(models.Model):
    nome = models.CharField('Nome do serviço', max_length=100)
    descricao = models.TextField('Descrição do Serviço')
    imagem = models.ImageField(upload_to = 'servicos/', default = 'servicos/default.png')

    def __str__(self):
        return self.nome