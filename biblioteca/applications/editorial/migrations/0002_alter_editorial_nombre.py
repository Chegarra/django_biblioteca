# Generated by Django 4.1.2 on 2022-10-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorial',
            name='nombre',
            field=models.CharField(max_length=32, unique=True, verbose_name='Editorial'),
        ),
    ]