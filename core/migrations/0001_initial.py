# Generated by Django 2.1.3 on 2018-11-23 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do serviço')),
                ('descricao', models.TextField(verbose_name='Descrição do Serviço')),
                ('imagem', models.ImageField(default='static/img/servicos/default.png', upload_to='static/img/servicos/')),
            ],
        ),
    ]
