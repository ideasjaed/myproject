# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Alumno.estado_proce'
        db.delete_column(u'inscripcion_alumno', 'estado_proce')

        # Adding field 'Alumno.estado_p'
        db.add_column(u'inscripcion_alumno', 'estado_p',
                      self.gf('django.db.models.fields.CharField')(default='Chiapas', max_length=32),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Alumno.estado_proce'
        db.add_column(u'inscripcion_alumno', 'estado_proce',
                      self.gf('django.db.models.fields.CharField')(default='Chiapas', max_length=32),
                      keep_default=False)

        # Deleting field 'Alumno.estado_p'
        db.delete_column(u'inscripcion_alumno', 'estado_p')


    models = {
        u'inscripcion.alumno': {
            'Meta': {'object_name': 'Alumno'},
            'ap_materno': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'ap_paterno': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'c_p': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'curp': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'direccion_p': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'escuela_p': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'estado': ('django.db.models.fields.CharField', [], {'default': "'Chiapas'", 'max_length': '32'}),
            'estado_civil': ('django.db.models.fields.CharField', [], {'default': "'Soltero'", 'max_length': '20'}),
            'estado_p': ('django.db.models.fields.CharField', [], {'default': "'Chiapas'", 'max_length': '32'}),
            'f_inscripcion': ('django.db.models.fields.DateField', [], {'auto_now': 'True', 'blank': 'True'}),
            'f_nacimiento': ('django.db.models.fields.DateField', [], {}),
            'fkcarrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publico.Carrera']", 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'matricula': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'municipio_p': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'telefono': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        u'publico.carrera': {
            'Meta': {'unique_together': "(('tipo', 'nombre'),)", 'object_name': 'Carrera'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'm_c': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'p_egreso': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'p_ingreso': ('django.db.models.fields.TextField', [], {'max_length': '200', 'blank': 'True'}),
            'requisitos': ('django.db.models.fields.TextField', [], {}),
            'tipo': ('django.db.models.fields.CharField', [], {'default': "'Licenciatura'", 'max_length': '32'})
        }
    }

    complete_apps = ['inscripcion']