# Generated by Django 4.1.2 on 2022-10-19 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='libro',
            options={'ordering': ['titulo'], 'verbose_name': 'Libro', 'verbose_name_plural': 'Libros'},
        ),
    ]
