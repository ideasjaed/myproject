# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Alumno'
        db.create_table(u'inscripcion_alumno', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fkcarrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publico.Carrera'], null=True, blank=True)),
            ('matricula', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ap_paterno', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('ap_materno', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('curp', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('f_nacimiento', self.gf('django.db.models.fields.DateField')()),
            ('estado_civil', self.gf('django.db.models.fields.CharField')(default='Soltero', max_length=20)),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('estado', self.gf('django.db.models.fields.CharField')(default='Chiapas', max_length=32)),
            ('telefono', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('escuela_p', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('direccion_p', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('municipio_p', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('estado_p', self.gf('django.db.models.fields.CharField')(default='Chiapas', max_length=32)),
            ('c_p', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('f_inscripcion', self.gf('django.db.models.fields.DateField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'inscripcion', ['Alumno'])


    def backwards(self, orm):
        # Deleting model 'Alumno'
        db.delete_table(u'inscripcion_alumno')


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