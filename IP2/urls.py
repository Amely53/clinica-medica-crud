
from django.contrib import admin
from django.urls import path
from Clinica import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='inicio'),
    path('pacientes', views.pacientes, name='pacientes'),
    path('verpacientes', views.verpacientes, name='verpacientes'),
    path('pacientes/guardar', views.guardar, name='guardar'),
    path('pacientes/eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('pacientes/detalle/<int:id>', views.detalle, name='detalle'),
    path('pacientes/editar', views.editar, name='editar'),
    path('medicos', views.medicos, name='medicos'),
    path('vermedicos', views.vermedicos, name='vermedicos'),
    path('medicos/guardar', views.guardarM, name='guardar'),
    path('medicos/eliminar/<int:id>', views.eliminarM, name='eliminarM'),
    path('medicos/detalle/<int:id>', views.detalleM, name='detalleM'),
    path('medicos/editar', views.editarM, name='modificar'),
    path('historia', views.historia, name='historia'),
    path('historia/guardar', views.historiaguardar, name='historiaguardar'),
    path('historia/eliminar/<int:id>', views.eliminarhistoria, name='eliminarhistoria'),
    path('historia/detalle/<int:id>', views.detallehistoria, name='detallehistoria'),
    path('historia/editar', views.editarhistoria, name='editarhistoria'),
    path('verhistoria', views.verhistoria, name='verhistoria'),  
    path('contacto', views.contacto, name='contacto'),
    path('contacto/guardar', views.contactoguardar, name='contactoguardar'),
    path('contacto/eliminar/<int:id>', views.eliminarcontacto, name='eliminarcontacto'),
    path('vercontacto', views.vercontacto, name='vercontacto'),
    path('info', views.info, name='info'),
]
