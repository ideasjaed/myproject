"""
from django.forms import ModelForm
from django import forms
#from publico.models import Alumno



class AlumnoForm(ModelForm):
	class Meta:
		model = Alumno
		fields = ('Ap_paterno','Ap_materno', 'Nombre', 'curp','fecha_nacimiento','estado_civil','direccion','estado','c_p','email','escuela_procedencia','direccion_procedencia', 'municipio', 'estado_procedencia','codigo_postal')



class ContactForm(forms.Form):
	name = forms.CharField(label=("Su Nombre"),max_length=255,widget=forms.TextInput,)
	correo = forms.EmailField(label='Tu correo electronico')
	mensaje = forms.CharField(widget= forms.Textarea)


class LoginForm(ModelForm):
	class Meta:
		model = Alumno

		"""