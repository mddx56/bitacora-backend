# Generated by Django 5.1.1 on 2024-09-29 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0007_alter_bank_logo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='period',
            field=models.CharField(choices=[('W', 'Semanal'), ('B', 'Quincenal'), ('M', 'Mensual'), ('O', 'Otro')], default='W', max_length=2, verbose_name='Frecuencia dia'),
        ),
    ]
