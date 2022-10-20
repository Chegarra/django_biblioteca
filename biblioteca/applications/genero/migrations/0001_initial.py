# Generated by Django 4.1.2 on 2022-10-19 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=32, unique=True, verbose_name='Género')),
                ('codigo', models.CharField(max_length=8, unique=True, verbose_name='Código')),
            ],
            options={
                'verbose_name': 'Género',
                'verbose_name_plural': 'Géneros',
                'ordering': ['nombre', 'codigo'],
            },
        ),
    ]
