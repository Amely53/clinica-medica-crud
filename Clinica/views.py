from django.shortcuts import render, redirect
from Clinica.models import Pacientes
from Clinica.models import Medicos
from Clinica.models import Historia
from Clinica.models import Contacto
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "principal.html")

def pacientes(request):
    pacientes = Pacientes.objects.all()
    return render(request, "pacientes.html",{'pacientes' : pacientes})

def verpacientes(request):
    verpacientes = Pacientes.objects.all()
    return render(request, "pacientesVer.html",{'pacientes' : verpacientes})

def medicos(request):
    medicos = Medicos.objects.all()
    return render(request, "medicos.html",{'medicos' : medicos})

def vermedicos(request):
    vermedicos = Medicos.objects.all()
    return render(request, "medicosVer.html",{'medicos' : vermedicos})

def info(request):
    return render(request, "info.html")

def guardar(request):
   nombre = request.POST["nombre"]
   dpi = request.POST["dpi"]
   fecha_de_nacimiento = request.POST["fecha_de_nacimiento"]
   dirección = request.POST["dirección"]
   razón_de_su_visita = request.POST["razón_de_su_visita"]
   receta_médica = request.POST["receta_médica"]
   número_telefónico = request.POST["número_telefónico"]
   p = Pacientes(nombre=nombre, dpi=dpi, fecha_de_nacimiento=fecha_de_nacimiento, dirección=dirección, razón_de_su_visita=razón_de_su_visita, receta_médica=receta_médica, número_telefónico=número_telefónico) 
   p.save()
   messages.success(request, 'Los datos del PACIENTE han sido AGREGADOS.')
   return redirect('pacientes')

def guardarM(request):
    nom = request.POST["nombre"]
    número_de_colegiado = request.POST["número_de_colegiado"]
    especialidad = request.POST["especialidad"]
    diagnóstico = request.POST["diagnóstico"]
    m = Medicos(nombre=nom, número_de_colegiado=número_de_colegiado, especialidad=especialidad, diagnóstico=diagnóstico)
    m.save()
    messages.success(request, 'Los datos del MÉDICO han sido AGREGADOS.')
    return redirect('medicos')

def eliminar(request, id):
    paciente = Pacientes.objects.filter(pk=id)
    paciente.delete()
    messages.success(request, 'Los datos del PACIENTE han sido ELIMINADOS.')
    return redirect('verpacientes')

def eliminarM(request, id):
    medico = Medicos.objects.filter(pk=id)
    medico.delete()
    messages.success(request, 'Los datos del MÉDICO han sido ELIMINADOS.')
    return redirect('vermedicos')

def detalle(request, id):
    paciente = Pacientes.objects.get(pk=id)
    return render(request, "pacientesEditar.html",{'paciente' : paciente})

def editar(request):
   nombre = request.POST["nombre"]
   dpi = request.POST["dpi"]
   fecha_de_nacimiento = request.POST["fecha_de_nacimiento"]
   dirección = request.POST["dirección"]
   razón_de_su_visita = request.POST["razón_de_su_visita"]
   receta_médica = request.POST["receta_médica"]
   número_telefónico = request.POST["número_telefónico"]
   id = request.POST["id"]
   Pacientes.objects.filter(pk=id).update(id=id, nombre=nombre, dpi=dpi, fecha_de_nacimiento=fecha_de_nacimiento, dirección=dirección, razón_de_su_visita=razón_de_su_visita, receta_médica=receta_médica, número_telefónico=número_telefónico)
   messages.success(request, 'Los datos del PACIENTE han sido ACTUALIZADOS.')
   return redirect('verpacientes')

def detalleM(request, id):
    medico = Medicos.objects.get(pk=id)
    return render(request, "medicosEditar.html",{'medico' : medico})

def editarM(request):
    nom = request.POST["nombre"]
    número_de_colegiado = request.POST["número_de_colegiado"]
    especialidad = request.POST["especialidad"]
    diagnóstico = request.POST["diagnóstico"]
    id = request.POST["id"]
    Medicos.objects.filter(pk=id).update(id=id, nombre=nom, número_de_colegiado=número_de_colegiado, especialidad=especialidad, diagnóstico=diagnóstico)
    messages.success(request, 'Los datos del MÉDICO han sido ACTUALIZADOS.')
    return redirect('vermedicos') 

def historia(request):
    historias = Historia.objects.all()
    return render(request, "historiaC.html", {'historias': historias})

def historiaguardar(request):
    medico = request.POST["médico"]
    paciente = request.POST["paciente"]
    nacimiento = request.POST["nacimiento"]
    genero = request.POST["género"]
    direccion = request.POST["dirección"]
    antecedentes = request.POST["antecedentes"]
    receta = request.POST["receta"]
    sintomas = request.POST["síntomas"]
    alergias = request.POST["alergias"]
    diagnostico = request.POST["diagnóstico"]
    hg = Historia(médico_tratante=medico, nombre_del_paciente=paciente, fecha_de_nacimiento=nacimiento, género=genero, dirección=direccion, antecedentes_médicos=antecedentes, receta_médica=receta, síntomas=sintomas, alergias=alergias, diagnóstico=diagnostico)
    hg.save()
    messages.success(request, 'Los datos del HISTORIAL clínico han sido AGREGADOS.')
    return redirect('historia')

def eliminarhistoria(request, id):
    eliminarhistoria = Historia.objects.filter(pk=id)
    eliminarhistoria.delete()
    messages.success(request, 'Los datos del HISTORIAL clínico han sido ELIMINADOS.')
    return redirect('verhistoria')

def detallehistoria(request, id):
    historia = Historia.objects.get(pk=id)
    return render(request, "historiaEditar.html",{'historia' : historia})

def editarhistoria(request):
    medico = request.POST["médico"]
    paciente = request.POST["paciente"]
    nacimiento = request.POST["nacimiento"]
    genero = request.POST["género"]
    direccion = request.POST["dirección"]
    antecedentes = request.POST["antecedentes"]
    receta = request.POST["receta"]
    sintomas = request.POST["síntomas"]
    alergias = request.POST["alergias"]
    diagnostico = request.POST["diagnóstico"]
    id = request.POST["id"]
    Historia.objects.filter(pk=id).update(id=id,médico_tratante=medico, nombre_del_paciente=paciente, fecha_de_nacimiento=nacimiento, género=genero, dirección=direccion, antecedentes_médicos=antecedentes, receta_médica=receta, síntomas=sintomas, alergias=alergias, diagnóstico=diagnostico)
    messages.success(request, 'Los datos del HISTORIAL clínico han sido ACTUALIZADOS.')
    return redirect('verhistoria')

def verhistoria(request):
    verhistoria = Historia.objects.all()
    return render(request, "historiaVer.html", {'historias' : verhistoria})

def contacto(request):
    contactos = Contacto.objects.all()
    return render(request, 'contacto.html', {'contactos' : contactos})

def contactoguardar(request):
    nombre = request.POST["nombre"]
    correo = request.POST["correo"]
    asunto = request.POST["asunto"]
    mensaje = request.POST["mensaje"]
    c = Contacto(nombre=nombre, correo_electrónico=correo, asunto=asunto, mensaje=mensaje)
    c.save()
    messages.success(request, 'MENSAJE enviado.')
    return redirect('contacto')

def eliminarcontacto(request, id):
    eliminarcontacto = Contacto.objects.filter(pk=id)
    eliminarcontacto.delete()
    messages.success(request, 'Mensaje de CONTACTO ELIMINADO.')
    return redirect('vercontacto')

def vercontacto(request):
    vercontacto = Contacto.objects.all()
    return render(request, "contactoVer.html", {'contactos' : vercontacto})