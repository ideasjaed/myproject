from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Slide(models.Model):
	titulo = models.CharField(max_length=100)
	contenido = models.TextField()
	fecha = models.DateTimeField(auto_now_add=True)
	def __unicode__ (self):
		return self.titulo

class Carrera(models.Model):
	LICENCIATURA = 'LC'
	TECNICA = 'TC'
	Tipos_de_Carreras=(
	(LICENCIATURA,'licenciatura'),
	(TECNICA,"Carrera Tecnica"),
	)
	Tipo = models.CharField(max_length=2,
		choices = Tipos_de_Carreras, 
		default=LICENCIATURA)
	Nombre = models.CharField(max_length=100)
	Perfil_egreso = models.TextField()
	perfil_ingreso = models.TextField()
	requisitos_ingreso=models.TextField()
	imagen = models.ImageField(upload_to='carrera',verbose_name='Image',blank=True)
	mapa_curricular = models.ImageField(upload_to='carrera',verbose_name='Image2',blank=True)
	def __unicode__(self):
		return self.Nombre

class Alumno(models.Model):
	Ap_paterno = models.CharField(max_length= 100,verbose_name='Apellido Paterno')
	Ap_materno = models.CharField(max_length=100 ,verbose_name='Apellido Materno')
	Nombre = models.CharField(max_length=100,verbose_name='Nombre(s)')
	curp = models.CharField(max_length=100,verbose_name='CURP')
	matricula = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	fecha_nacimiento = models.DateField()
	estado_civil = models.CharField(max_length=100,verbose_name='Estado Civil')
	direccion = models.TextField(verbose_name='Direccion')
	estado = models.CharField(max_length=100,verbose_name='Estado')
	c_p = models.CharField(max_length=100,verbose_name='Codiogo Postal')
	telefono = models.CharField(max_length=100,verbose_name='Telefono')
	email = models.CharField(max_length=100,verbose_name='Correo Electronico')
	escuela_procedencia = models.CharField(max_length=100,verbose_name='Nombre de la Escuela de Procedencia')
	direccion_procedencia = models.TextField(verbose_name='Direccion de la Escuela de Procedencia')
	municipio = models.CharField(max_length=100,verbose_name='Municipio de la Escuela de Procedencia')
	estado_procedencia = models.CharField(max_length=100,verbose_name='Estado de la Escuela de Procedencia')
	codigo_postal = models.CharField(max_length=100,verbose_name='Codiogo Postal de la Escuela de Procedencia')
	inscrito = 'IN'
	no_inscrito = 'NOI'
	Inscrito=(
	(no_inscrito,"no_Inscrito"),
	(inscrito,'inscrito'),
	)
	Tipo = models.CharField(max_length=20,
		choices = Inscrito, 
		default=Inscrito)

	def get_foo():
    		return User.objects.get(id=1)
	user = models.ForeignKey(User, default=get_foo)
	
	grado = models.CharField(max_length=20)
	grupo = models.CharField(max_length=20)
	def get_foo2():
    		return Carrera.objects.get(id=1)
	Nombre_carrera = models.ForeignKey(Carrera,default=get_foo2)

	





	def __unicode__(self):
		return self.Ap_paterno

class Materia(models.Model):
	
	Nombre = models.CharField(max_length=100)
	Nombre_carrera = models.ForeignKey(Carrera)

	def __unicode__(self):
		return self.Nombre





class Calificacione(models.Model):
	alumno = models.ForeignKey(Alumno)
	
	cal0 = 'cala'
	cal1 = 'Calb'
	cal2 = 'Calc'
	cal3 = 'Cald'
	cal4 = 'Cale'
	cal5 = 'Calf'
	cal6 = 'Calg'
	cal7 = 'Calh'
	cal8 = 'Cali'
	cal9 = 'Calj'
	cal10 = 'Calk'

	califica=(
	(cal0,'0'),
	(cal1,"1"),
	(cal2,"2"),
	(cal3,"3"),
	(cal4,"4"),
	(cal5,"5"),
	(cal6,"6"),
	(cal7,"7"),
	(cal8,"8"),
	(cal9,"9"),
	(cal10,"10"),)
	Calificacion = models.CharField(max_length=5,
		choices = califica, 
		default=cal0)
	Nombre_materia = models.ForeignKey(Materia)
	def __unicode__(self):
		return self.Calificacion




class Docente(models.Model):
	A_paterno = models.CharField(max_length= 100,verbose_name='Apellido Paterno')
	A_materno = models.CharField(max_length=100 ,verbose_name='Apellido Materno')
	Nombre = models.CharField(max_length=100,verbose_name='Nombre(s)')

	def __unicode__(self):
		return self.Nombre