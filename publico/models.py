from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Slide(models.Model):
	titulo = models.CharField(max_length=100)
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)
	imagen = models.ImageField(upload_to='carrera',verbose_name='imagen slite',blank=True)
	def __unicode__ (self):
		return self.titulo

class Carrera(models.Model):
	li         = ['Licenciatura','Tecnico','Preparatoria','Idiomas']
	lis        = ((li[0],li[0]),(li[1],li[1]),(li[2],li[2]),(li[3],li[3]),)
	tipo       = models.CharField(max_length=32,choices=lis,default=li[0])
	nombre     = models.CharField('Nombre de la Carrera', max_length = 200)
	p_ingreso  = models.TextField('Perfil de Ingreso',max_length = 200,blank=True)
	p_egreso   = models.TextField('Perfil de Egreso ',max_length = 200,blank=True)
	requisitos = models.TextField()
	imagen     = models.ImageField(upload_to='carrera',verbose_name ='Image',blank=True)
	m_c        = models.ImageField(upload_to='carrera',verbose_name ='Image2',blank=True)

	class Meta:
		unique_together = ("tipo", "nombre")

	def __unicode__(self):
		return self.nombre
