# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'App'
        db.create_table(u'stack_app', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('official_site', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'stack', ['App'])

        # Adding model 'Category'
        db.create_table(u'stack_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('description', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'stack', ['Category'])

        # Adding model 'AppStack'
        db.create_table(u'stack_appstack', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app', self.gf('django.db.models.fields.related.ForeignKey')(related_name='apps+', to=orm['stack.App'])),
            ('stack', self.gf('django.db.models.fields.related.ForeignKey')(related_name='stacks+', to=orm['stack.App'])),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stack.Category'], null=True, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('used_since', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('used_until', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('created_at', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modified_at', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
        ))
        db.send_create_signal(u'stack', ['AppStack'])


    def backwards(self, orm):
        # Deleting model 'App'
        db.delete_table(u'stack_app')

        # Deleting model 'Category'
        db.delete_table(u'stack_category')

        # Deleting model 'AppStack'
        db.delete_table(u'stack_appstack')


    models = {
        u'stack.app': {
            'Meta': {'object_name': 'App'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'official_site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'stacks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stack.App']", 'through': u"orm['stack.AppStack']", 'symmetrical': 'False'})
        },
        u'stack.appstack': {
            'Meta': {'object_name': 'AppStack'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apps+'", 'to': u"orm['stack.App']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stack.Category']", 'null': 'True', 'blank': 'True'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'stack': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stacks+'", 'to': u"orm['stack.App']"}),
            'used_since': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'used_until': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'stack.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['stack']