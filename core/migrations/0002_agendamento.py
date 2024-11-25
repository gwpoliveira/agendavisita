# Generated by Django 5.1.3 on 2024-11-11 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(max_length=20)),
                ('unidade', models.CharField(choices=[('Primavera', 'Primavera'), ('Bela Vista', 'Bela Vista')], max_length=50)),
                ('data', models.DateField()),
                ('hora', models.TimeField()),
                ('status', models.CharField(choices=[('Agendado', 'Agendado'), ('Realizado', 'Realizado'), ('Cancelado', 'Cancelado')], default='Agendado', max_length=20)),
                ('observacoes', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
