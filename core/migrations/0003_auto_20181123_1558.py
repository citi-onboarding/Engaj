# Generated by Django 2.1.3 on 2018-11-23 18:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20181123_1257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='imagem',
            field=models.ImageField(default='servicos/default.jpg', upload_to='servicos/'),
        ),
    ]
