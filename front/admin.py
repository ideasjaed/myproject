from django.contrib import admin
from models import *



class PostAdmin(admin.ModelAdmin):
	prepopulated_fields = {"Ap_paterno": ("Nombre",)}
	
	
	list_display = ['Nombre','Ap_paterno','Ap_materno','curp']
	list_filter = ['estado','Tipo']
	search_fields = ('Nombre','direccion',)
	


class PostAdmind(admin.ModelAdmin):
	prepopulated_fields = {"Nombre": ("Perfil_egreso",)}
	
	
	list_display = ['Nombre',]
	list_filter = ['Nombre',]
	search_fields = ('Nombre','Perfil_egreso','Ap_paterno',)
	

admin.site.register(Slide)
admin.site.register(Alumno,PostAdmin)
admin.site.register(Carrera,PostAdmind)
admin.site.register(Materia)
admin.site.register(Calificacione)
admin.site.register(Docente)

