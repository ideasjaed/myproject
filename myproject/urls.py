from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
{
                'document_root': settings.MEDIA_ROOT,
            }), 
	)

urlpatterns += patterns('publico.views',
    
	url(r'^$', 'index'),
	url(r'^ofertaEducativa/$','ofertaEducativa'),
	url(r'^nosotros/$','nosotros'),
	url(r'^directorio/$','directorio'),
	url(r'^contacto/$','contacto'),
	url(r'^login/$', 'login_v'),
	url(r'^ingresar/$', 'ingresar'),
	url(r'^icos/$','ico'),

	
	url(r'^pdf$','pdf'),

	##SAED
	url(r'^SAED/$','SAED'),
	url(r'^SAED/calificaciones/$','SAED_calif'),
	url(r'^SAED/calendario/$','SAED_Calend'),	
	url(r'^SAED/configuracion/$','SAED_Config'),	
	url(r'^SAED/encuestas/$','SAED_encuestas'),
	url(r'^SAED/informacion/$','SAED_informacion'),	
	url(r'^SAED/inscripciones/$','SAED_inscripcion'),
				

     	 )	


urlpatterns += patterns('inscripcion.views',
	url(r'^inscripcion/licenciatura/$','ins_Lic'),
	url(r'^inscripcion/tecnico/$','ins_Tec'),
	url(r'^inscripcion/idioma/$','ins_Idioma'),
	url(r'^inscripcion/preparatoria/$','ins_Prepa'),
	#url(r'^inscripciones/)
	)
