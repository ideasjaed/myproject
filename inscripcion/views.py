from django.shortcuts import render_to_response , get_object_or_404
from django.template import  RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from inscripcion.models import Alumno, Carrera
from django import forms
from django.forms import ModelForm





class AlumnoForm(ModelForm):
	class Meta:
		model = Alumno
		fields = ('ap_paterno','ap_materno','nombre','curp','f_nacimiento','estado_civil','direccion','estado','c_p','telefono','email','escuela_p','direccion_p','municipio_p','estado_p','c_p')

def ins_Lic(request):
        i = Carrera.objects.get(tipo="Licenciatura");
        if request.method == "POST":
                formulario = AlumnoForm(request.POST, request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        formulari = Alumno.objects.order_by('-pk')[0] 
                        formulari.fkcarrera = i
                        formulari.save()
                        return render_to_response("inscripcion/FichaLicenciatura.html",{'form':formulari},context_instance=RequestContext(request))
        else:
                formulario = AlumnoForm()
        return render_to_response("inscripcion/inscripcion.html",{'formulario':formulario,'C':i},context_instance=RequestContext(request))


def ins_Tec(request):
        i = Carrera.objects.get(tipo="Tecnico")
        if request.method == "POST":
                formulario = AlumnoForm(request.POST, request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        formulari = Alumno.objects.order_by('-pk')[0] 
                        formulari.fkcarrera = i
                        formulari.save()
                        return render_to_response("inscripcion/FichaTecnico.html",{'form':formulari},context_instance=RequestContext(request))
        else:
                formulario = AlumnoForm()
        return render_to_response("inscripcion/inscripcion.html",{'formulario':formulario,'C':i},context_instance=RequestContext(request))


def ins_Idioma(request):
        i = Carrera.objects.get(tipo="Idiomas");
        if request.method == "POST":
                formulario = AlumnoForm(request.POST, request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        formulari = Alumno.objects.order_by('-pk')[0] 
                        formulari.fkcarrera = i
                        formulari.save()
                        return render_to_response("inscripcion/FichaIngles.html",{'form':formulari},context_instance=RequestContext(request))
        else:
                formulario = AlumnoForm()
        return render_to_response("inscripcion/inscripcion.html",{'formulario':formulario,'C':i},context_instance=RequestContext(request))

def ins_Prepa(request):
        i = Carrera.objects.get(tipo="Preparatoria")
        if request.method == "POST":
                formulario = AlumnoForm(request.POST, request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        formulari = Alumno.objects.order_by('-pk')[0] 
                        formulari.fkcarrera = i
                        formulari.save()
                        return render_to_response("inscripcion/FichaPrepa.html",{'form':formulari},context_instance=RequestContext(request))
        else:
                formulario = AlumnoForm()
        return render_to_response("inscripcion/inscripcion.html",{'formulario':formulario,'C':i},context_instance=RequestContext(request))