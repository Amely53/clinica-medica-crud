from django.contrib import admin
from Clinica.models import Pacientes
from Clinica.models import Medicos
from Clinica.models import Historia
from Clinica.models import Contacto

# Register your models here.
admin.site.register(Pacientes),
admin.site.register(Medicos),
admin.site.register(Historia),
admin.site.register(Contacto)
