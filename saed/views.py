from django.shortcuts import render_to_response , get_object_or_404
from django.template import  RequestContext
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from saed.models import *


def directorio(request):
	docente = Docente.objects.all()
        return render_to_response("SAED/directorio.html",{'docente':docente}, context_instance=RequestContext(request))