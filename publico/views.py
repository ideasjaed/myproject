# -*- encoding: utf-8 -*-
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.core.urlresolvers import reverse
from django.core.mail import EmailMessage
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import (REDIRECT_FIELD_NAME, login, logout, authenticate)
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response , get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.template import  RequestContext
from django.views.generic.edit import FormView
from publico.models import Slide, Carrera
from publico.forms import *
from reportlab.pdfgen import canvas
from io import BytesIO
from django import forms
#from publico.forms import LoginForm
import urlparse
import os


class ContactForm(forms.Form):
	name = forms.CharField(label=("Su Nombre"),max_length=255,widget=forms.TextInput,)
	correo = forms.EmailField(label='Tu correo electronico')
	mensaje = forms.CharField(widget= forms.Textarea)



def index(request):
        slide = Slide.objects.all().order_by("-fecha")
        return render_to_response("index.html",{'s':slide}, context_instance=RequestContext(request))

def ofertaEducativa(request):
        carrera = Carrera.objects.all()
        return render_to_response("ofertaEducativa.html",{'datos':carrera}, context_instance=RequestContext(request))

def nosotros(request):
		return render_to_response("nosotros.html", context_instance=RequestContext(request))

def directorio(request):
        return render_to_response("directorio.html", context_instance=RequestContext(request))

def login_v(request):
        return render_to_response("login.html", context_instance=RequestContext(request))

def contacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            titulo = 'Mensaje desde el Sistema Cesic'
            contenido = form.cleaned_data['mensaje']+"\n"
            
            contenido+='Comunicarse a: '+form.cleaned_data['correo']
            correo = EmailMessage  (titulo ,contenido,to=['sistemacesic@gmail.com'])
            correo.send()
        return HttpResponseRedirect('/contacto')
    
    else:
        form=ContactForm()
        return render_to_response('contacto.html', {'form':form,},context_instance=RequestContext(request))


def SAED(request):
                return render_to_response("SAED_inicio.html", context_instance=RequestContext(request))


@login_required(login_url='/login')
def SAED_calif(request):
        user=request.user.id
        info = Alumno.objects.get(id=user)
        calificacion = Calificacione.objects.all()
        return render_to_response("SAED_calificaciones.html",{'cal':info,'mate':calificacion}, context_instance=RequestContext(request))

def SAED_Calend(request):
                return render_to_response("SAED_calendario.html", context_instance=RequestContext(request))

def SAED_Config(request):
                return render_to_response("SAED_configuracion.html", context_instance=RequestContext(request))

def SAED_encuestas(request):
                return render_to_response("SAED_encuestas.html", context_instance=RequestContext(request))

def SAED_informacion(request):
                return render_to_response("SAED_informacion.html", context_instance=RequestContext(request))

def SAED_inscripcion(request):
                return render_to_response("SAED_inscripciones.html", context_instance=RequestContext(request))

def agregar_alumno(request):
        if request.method == "POST":
                formulario = AlumnoForm(request.POST, request.FILES)
                if formulario.is_valid():
                        formulario.save()
                        formulari = Alumno.objects.order_by('-pk')[0] 
                        return render_to_response("FichaIESUM.html",{'form':formulari},context_instance=RequestContext(request))
        else:
                formulario = AlumnoForm()
        return render_to_response("inicripcion.html",{'formulario':formulario},context_instance=RequestContext(request))


def pdf(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='publico/pdf')
    response['Content-Disposition'] = 'attachment; filename="ficha.pdf"'

    buffer = BytesIO()

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, "Hello world.")
    

    
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response


def ingresar(request):
    if request.method == 'POST':
        formu = AuthenticationForm(request.POST)
        if formu.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return render_to_response('SAED_inicio.html',{'ful_name':request.user.username},context_instance=RequestContext(request))
                else:
                    return render_to_response('noactivo.html',context_instance=RequestContext(request))
            else:
                return render_to_response('nosusuario.html',context_instance=RequestContext(request))        
    else:
        formu = AuthenticationForm()
        return HttpResponseRedirect('/')
        



def Ficha(request):
    return render_to_response("FichaIESUM.html", context_instance=RequestContext(request))