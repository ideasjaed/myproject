# -*- encoding: utf-8 -*-
from django.db import models
from publico.models import Carrera

class Alumno(models.Model):
	ec=['Soltero','Casado','Union Libre']
	ecl= ((ec[0],ec[0]),(ec[1],ec[1]),(ec[2],ec[2]),)
	edo=['Aguascalientes',
        'Baja California',
        'Baja California Sur',
        'Campeche',
        'Coahuila',
        'Colima',
        'Chiapas',
        'Chihuahua',
        'Distrito Federal',
        'Durango',
        'Guanajuato',
        'Guerrero',
        'Hidalgo',
        'Jalisco',
        'México',
        'Michoacán',
        'Morelos',
        'Nayarit',
        'Nuevo León',
        'Oaxaca',
        'Puebla',
        'Querétaro',
        'Quintana Roo',
        'San Luis Potosí',
        'Sinaloa',
        'Sonora',
        'Tabasco',
        'Tamaulipas',
        'Tlaxcala',
        'Veracruz',
        'Yucatán',
        'Zacatecas']
        edo_=((edo[0],edo[0]),(edo[1],edo[1]),(edo[2],edo[2]),(edo[3],edo[3]),(edo[4],edo[4]),(edo[5],edo[5]),(edo[6],edo[6]),(edo[7],edo[7]),(edo[8],edo[8]),(edo[9],edo[9]),(edo[10],edo[10]),(edo[11],edo[11]),(edo[12],edo[12]),(edo[13],edo[13]),(edo[14],edo[14]),(edo[15],edo[15]),(edo[16],edo[16]),(edo[17],edo[17]),(edo[18],edo[18]),(edo[19],edo[19]),(edo[20],edo[20]),(edo[21],edo[21]),(edo[22],edo[22]),(edo[23],edo[23]),(edo[24],edo[24]),(edo[25],edo[25]),(edo[26],edo[26]),(edo[27],edo[27]),(edo[28],edo[28]),(edo[29],edo[29]),(edo[30],edo[30]),(edo[31],edo[31]),)

        fkcarrera    = models.ForeignKey(Carrera,verbose_name='Carrera',blank=True,null=True)
        matricula    = models.CharField(max_length=100,blank=True)
        password     = models.CharField(max_length=100, verbose_name='Contraseña')
        ap_paterno   = models.CharField(max_length=100, verbose_name='Apellido Paterno')
        ap_materno   = models.CharField(max_length=100, verbose_name='Apellido Materno',blank=True,null=True)
        nombre       = models.CharField(max_length=100, verbose_name='Nombre(s)')
        curp         = models.CharField(max_length=100)
        f_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento')
        estado_civil = models.CharField(max_length=20,choices=ecl, default=ec[0])
        direccion    = models.TextField(verbose_name='Direccion')
        estado       = models.CharField('Estado', max_length=32,choices=edo_,default=edo[6])
        c_p          = models.CharField(max_length=100,verbose_name='Codiogo Postal')
        telefono     = models.CharField(max_length=100,verbose_name='Telefono',blank=True,null=True)
        email        = models.CharField(max_length=100,verbose_name='Correo Electronico',blank=True,null=True)
        escuela_p    = models.CharField(max_length=100,verbose_name='Nombre de la Escuela de Procedencia',blank=True,null=True)
        direccion_p  = models.TextField(verbose_name='Direccion de la Escuela de Procedencia',blank=True,null=True)
        municipio_p  = models.CharField(max_length=100,verbose_name='Municipio de la Escuela de Procedencia',blank=True,null=True)
        estado_p     = models.CharField('Estado de Escuela de Procedencia', max_length=32,choices=edo_,default=edo[6])
        c_p          = models.CharField(max_length=100,verbose_name='Codiogo Postal de la Escuela de Procedencia',blank=True,null=True)

	def __unicode__(self):
		return '%s  %s | %s'%(self.ap_paterno,self.nombre,self.matricula)
			#Que aqui aparesca el nombre y apellido paterno

class statu(models.Model):
	vst = ['Inscrito','No Inscrito','Regular','Irregular','Baja Temporal','Baja Definitiva','Titulado','Tramites de Titulacion']
	vstat =((vst[0],vst[0]),
			(vst[1],vst[1]),
			(vst[2],vst[2]),
			(vst[3],vst[3]),
			(vst[4],vst[4]),
			(vst[5],vst[5]),
			(vst[6],vst[6]),
			(vst[7],vst[7]),
		)
	alumno        = models.ForeignKey(Alumno)
	status        = models.CharField(max_length=30, choices=vstat, default= vst[2])
	f_inscripcion = models.DateField(auto_now=True)

	def __unicode__(self):
		return '%s  %s ' %(self.status,self.alumno)
