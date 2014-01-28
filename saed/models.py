from django.db import models
from publico.models import Carrera

class Docente(models.Model):
	Nombre         = models.CharField(max_length=200)
	estudios       = models.CharField('estudios universitarios',max_length=100,help_text='licenciatura o carrera tecnica')
	especialidad   = models.CharField(max_length=100,help_text='especialidad como maestria u doctorado')
	especialidad_2 = models.CharField('otra especialidad',max_length=100, help_text='en caso de tener mas especialidades llenar este campo',blank=True,null=True)
	especialidad_3 = models.CharField('otra especialidad',max_length=100, help_text='en caso de tener mas especialidades llenar este campo',blank=True,null=True)
	foto           = models.ImageField(upload_to='docentes',verbose_name=u'Fotografia',blank=True)

	def __unicode__(self):
		return self.Nombre

class Materia(models.Model):
	nombre    = models.CharField(max_length=200)
	fkcarrera = models.ForeignKey(Carrera)
	
	def __unicode__(self):
		return 'Materia: %s de la Carrera:%s'%(self.nombre,self.fkcarrera)

class Calificacion(models.Model):
	CHOICES      = [(i,i) for i in range(11)]
	parcial      = models.IntegerField('parcial / Unidad',max_length=10, choices=CHOICES)
	fkmateria    = models.ForeignKey(Materia)
	calificacion = models.DecimalField(max_digits=4, decimal_places=2)

	def __unicode__(self):
		return '%s %s' %(self.fkmateria,self.parcial)

