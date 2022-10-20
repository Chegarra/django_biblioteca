# Generated by Django 4.1.2 on 2022-10-19 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('genero', '0001_initial'),
        ('editorial', '0001_initial'),
        ('ubicacion', '0001_initial'),
        ('autor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=64, verbose_name='Título')),
                ('isbn', models.CharField(max_length=16, unique=True, verbose_name='ISBN')),
                ('resumen', models.CharField(blank=True, max_length=1024, verbose_name='Resumen')),
                ('nombre', models.CharField(max_length=32, unique=True, verbose_name='Género')),
                ('codigo', models.CharField(max_length=8, unique=True, verbose_name='Código')),
                ('autor', models.ManyToManyField(to='autor.autor')),
                ('editorial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='editorial.editorial')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='genero.genero')),
                ('ubicacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ubicacion.ubicacion')),
            ],
            options={
                'verbose_name': 'Libro',
                'verbose_name_plural': 'Libros',
                'ordering': ['titulo', 'autor__apellidos'],
            },
        ),
    ]
