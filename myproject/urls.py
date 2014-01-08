from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()


urlpatterns = patterns('',

#	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', 'front.views.index'),
	url(r'^ofertaEducativa/$','front.views.ofertaEducativa'),
	url(r'^nosotros/$','front.views.nosotros'),
	url(r'^directorio/$','front.views.directorio'),
	url(r'^contacto/$','front.views.contacto'),
	url(r'^login/$', 'front.views.login_v'),
	url(r'^ingresar/$', 'front.views.ingresar'),
	url(r'^Ficha/$','front.views.Ficha'),




	url(r'^alumno/nuevo/$','front.views.agregar_alumno'),
	url(r'^pdf$','front.views.pdf'),


	##SAED
	url(r'^SAED/$','front.views.SAED'),
	url(r'^SAED/calificaciones/$','front.views.SAED_calif'),
	url(r'^SAED/calendario/$','front.views.SAED_Calend'),	
	url(r'^SAED/configuracion/$','front.views.SAED_Config'),	
	url(r'^SAED/encuestas/$','front.views.SAED_encuestas'),
	url(r'^SAED/informacion/$','front.views.SAED_informacion'),	
	url(r'^SAED/inscripciones/$','front.views.SAED_inscripcion'),

            url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
{
                'document_root': settings.MEDIA_ROOT,
            }), 
	)	