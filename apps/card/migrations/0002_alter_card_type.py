# Generated by Django 5.1.1 on 2024-09-19 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(blank=True, choices=[('D', 'Debit'), ('C', 'Credit')], default='C', max_length=2, null=True, verbose_name='Tipo de tarjeta'),
        ),
    ]
