# Generated by Django 2.1.3 on 2019-01-11 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20181224_1421'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='imagem',
            field=models.ImageField(default='defaults/banner.png', upload_to='banner/'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='facebook',
            field=models.TextField(default='http://fb.me/MinhaPagina', verbose_name='Perfil no Facebook'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='imagem',
            field=models.ImageField(default='defaults/card.png', upload_to='servicos/'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='imagem',
            field=models.ImageField(default='defaults/banner.png', upload_to='sobre/', verbose_name='Imagem Institucional'),
        ),
    ]
