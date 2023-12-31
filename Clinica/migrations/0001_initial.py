# Generated by Django 4.2.6 on 2023-11-02 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Medicos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('número_de_colegiado', models.FloatField()),
                ('especialidad', models.CharField(max_length=50)),
                ('diagnóstico', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('dpi', models.FloatField()),
                ('fecha_de_nacimiento', models.CharField(max_length=50)),
                ('dirección', models.CharField(max_length=100)),
                ('razón_de_su_visita', models.CharField(max_length=100)),
                ('receta_médica', models.CharField(max_length=70)),
                ('número_telefónico', models.FloatField()),
            ],
        ),
    ]
