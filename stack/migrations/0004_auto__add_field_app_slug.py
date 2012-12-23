# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'App.slug'
        db.add_column(u'stack_app', 'slug',
                      self.gf('django.db.models.fields.SlugField')(default='stack', max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'App.slug'
        db.delete_column(u'stack_app', 'slug')


    models = {
        u'stack.app': {
            'Meta': {'object_name': 'App'},
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'official_site': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
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