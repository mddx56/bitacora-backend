# Generated by Django 5.1.1 on 2024-09-13 03:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.BooleanField(default=False)),
                ('card_number', models.CharField(max_length=250, unique=True, verbose_name='Número de tarjeta.')),
                ('holder', models.CharField(max_length=600, verbose_name='Titular de la tarjeta')),
                ('expiration_date', models.DateField(verbose_name='Fecha de expiracion')),
                ('cvv', models.CharField(max_length=3, verbose_name='CVV')),
                ('type', models.CharField(blank=True, max_length=56, null=True, verbose_name='Tipo de tarjeta')),
                ('credit_limit', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Límite de credito')),
                ('current_balance', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Saldo actual')),
                ('status', models.CharField(blank=True, choices=[('A', 'Active'), ('I', 'Inactive')], default='A', max_length=1, null=True, verbose_name='Estado de la tarjeta')),
                ('issue_date', models.DateField(blank=True, null=True, verbose_name='Fecha de emision')),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bank.bank', verbose_name='Banco')),
            ],
            options={
                'verbose_name': 'Tarjeta de credito',
                'verbose_name_plural': 'Tarjetas de credito',
            },
        ),
    ]
