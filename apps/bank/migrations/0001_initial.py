# Generated by Django 5.1.1 on 2024-09-13 03:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('deleted_at', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=350, verbose_name='Nombre de banco')),
                ('logo', models.URLField(verbose_name='Url Logo')),
            ],
            options={
                'verbose_name': 'Banco',
                'verbose_name_plural': 'Bancos',
            },
        ),
    ]
