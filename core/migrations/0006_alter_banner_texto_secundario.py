# Generated by Django 5.1.3 on 2024-11-19 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_agendamento_unidade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='texto_secundario',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]