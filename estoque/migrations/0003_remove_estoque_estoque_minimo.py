# Generated by Django 5.0.4 on 2024-04-16 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('estoque', '0002_minhaimagem_estoque_imagem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estoque',
            name='estoque_minimo',
        ),
    ]
