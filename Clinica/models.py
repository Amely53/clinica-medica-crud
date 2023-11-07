from django.db import models

# Create your models here.

class Pacientes(models.Model):

    nombre = models.CharField(max_length=50)
    dpi = models.CharField(max_length=20)
    fecha_de_nacimiento = models.CharField(max_length=50) 
    dirección = models.CharField(max_length=100)
    razón_de_su_visita = models.CharField(max_length=100)
    receta_médica = models.CharField(max_length=70)
    número_telefónico = models.CharField(max_length=20)

class Medicos(models.Model):

    nombre = models.CharField(max_length=50)
    número_de_colegiado = models.CharField(max_length=20)
    especialidad = models.CharField(max_length=50)
    diagnóstico = models.CharField(max_length=100)

class Historia(models.Model):

    médico_tratante = models.CharField(max_length=30)
    nombre_del_paciente = models.CharField(max_length=50)
    fecha_de_nacimiento = models.CharField(max_length=30)
    género = models.CharField(max_length=30)
    dirección = models.CharField(max_length=50)
    antecedentes_médicos = models.CharField(max_length=50)
    receta_médica = models.CharField(max_length=100)
    síntomas = models.CharField(max_length=50)
    alergias = models.CharField(max_length=30)
    diagnóstico = models.CharField(max_length=100)

class Contacto(models.Model):

    nombre = models.CharField(max_length=50)
    correo_electrónico = models.CharField(max_length=40)
    asunto = models.CharField(max_length=60)
    mensaje = models.CharField(max_length=170)
