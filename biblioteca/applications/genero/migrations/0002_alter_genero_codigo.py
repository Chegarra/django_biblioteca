# Generated by Django 4.1.2 on 2022-10-19 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('genero', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='codigo',
            field=models.CharField(max_length=16, unique=True, verbose_name='Código'),
        ),
    ]
