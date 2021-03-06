# Generated by Django 2.1.7 on 2019-05-26 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0005_auto_20190525_1325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='membros',
            options={'verbose_name': 'Membros', 'verbose_name_plural': 'Membros'},
        ),
        migrations.AlterField(
            model_name='membros',
            name='inviter',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='membros_convidados', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='membros',
            unique_together={('usuario', 'racha')},
        ),
    ]
