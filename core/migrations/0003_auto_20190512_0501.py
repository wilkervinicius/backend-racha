# Generated by Django 2.1.7 on 2019-05-12 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190406_1315'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='racha',
            name='aprovado',
        ),
        migrations.RemoveField(
            model_name='racha',
            name='usuario',
        ),
        migrations.AlterField(
            model_name='racha',
            name='descricao',
            field=models.TextField(blank=True, null=True, verbose_name='Descrição'),
        ),
    ]
