# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Docente'
        db.create_table(u'saed_docente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('Nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('estudios', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('especialidad', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('especialidad_2', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('especialidad_3', self.gf('django.db.models.fields.CharField')(max_length=100, null=True, blank=True)),
            ('foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'saed', ['Docente'])

        # Adding model 'Materia'
        db.create_table(u'saed_materia', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('fkcarrera', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['publico.Carrera'])),
        ))
        db.send_create_signal(u'saed', ['Materia'])

        # Adding model 'Calificacion'
        db.create_table(u'saed_calificacion', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('parcial', self.gf('django.db.models.fields.IntegerField')(max_length=10)),
            ('fkmateria', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['saed.Materia'])),
            ('calificacion', self.gf('django.db.models.fields.DecimalField')(max_digits=4, decimal_places=2)),
        ))
        db.send_create_signal(u'saed', ['Calificacion'])


    def backwards(self, orm):
        # Deleting model 'Docente'
        db.delete_table(u'saed_docente')

        # Deleting model 'Materia'
        db.delete_table(u'saed_materia')

        # Deleting model 'Calificacion'
        db.delete_table(u'saed_calificacion')


    models = {
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
        },
        u'saed.calificacion': {
            'Meta': {'object_name': 'Calificacion'},
            'calificacion': ('django.db.models.fields.DecimalField', [], {'max_digits': '4', 'decimal_places': '2'}),
            'fkmateria': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['saed.Materia']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'parcial': ('django.db.models.fields.IntegerField', [], {'max_length': '10'})
        },
        u'saed.docente': {
            'Meta': {'object_name': 'Docente'},
            'Nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'especialidad': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'especialidad_2': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'especialidad_3': ('django.db.models.fields.CharField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'estudios': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        u'saed.materia': {
            'Meta': {'object_name': 'Materia'},
            'fkcarrera': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['publico.Carrera']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['saed']