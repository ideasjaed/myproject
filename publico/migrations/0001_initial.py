# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Slide'
        db.create_table(u'publico_slide', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('titulo', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contenido', self.gf('django.db.models.fields.TextField')()),
            ('fecha', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'publico', ['Slide'])

        # Adding model 'Carrera'
        db.create_table(u'publico_carrera', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tipo', self.gf('django.db.models.fields.CharField')(default='Licenciatura', max_length=32)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('p_ingreso', self.gf('django.db.models.fields.TextField')(max_length=200, blank=True)),
            ('p_egreso', self.gf('django.db.models.fields.TextField')(max_length=200, blank=True)),
            ('requisitos', self.gf('django.db.models.fields.TextField')()),
            ('imagen', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('m_c', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
        ))
        db.send_create_signal(u'publico', ['Carrera'])

        # Adding unique constraint on 'Carrera', fields ['tipo', 'nombre']
        db.create_unique(u'publico_carrera', ['tipo', 'nombre'])


    def backwards(self, orm):
        # Removing unique constraint on 'Carrera', fields ['tipo', 'nombre']
        db.delete_unique(u'publico_carrera', ['tipo', 'nombre'])

        # Deleting model 'Slide'
        db.delete_table(u'publico_slide')

        # Deleting model 'Carrera'
        db.delete_table(u'publico_carrera')


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
        u'publico.slide': {
            'Meta': {'object_name': 'Slide'},
            'contenido': ('django.db.models.fields.TextField', [], {}),
            'fecha': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'imagen': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'titulo': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['publico']