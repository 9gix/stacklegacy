# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Category.slug'
        db.add_column(u'stack_category', 'slug',
                      self.gf('django.db.models.fields.SlugField')(max_length=50, unique=True, null=True),
                      keep_default=False)

        # Adding M2M table for field categories on 'App'
        db.create_table(u'stack_app_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('app', models.ForeignKey(orm[u'stack.app'], null=False)),
            ('category', models.ForeignKey(orm[u'stack.category'], null=False))
        ))
        db.create_unique(u'stack_app_categories', ['app_id', 'category_id'])

        # Deleting field 'AppStack.category'
        db.delete_column(u'stack_appstack', 'category_id')


    def backwards(self, orm):
        # Deleting field 'Category.slug'
        db.delete_column(u'stack_category', 'slug')

        # Removing M2M table for field categories on 'App'
        db.delete_table('stack_app_categories')

        # Adding field 'AppStack.category'
        db.add_column(u'stack_appstack', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['stack.Category'], null=True, blank=True),
                      keep_default=False)


    models = {
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'ref.reference': {
            'Meta': {'object_name': 'Reference'},
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'object_id': ('django.db.models.fields.PositiveIntegerField', [], {}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200'})
        },
        u'stack.app': {
            'Meta': {'object_name': 'App'},
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stack.Category']", 'symmetrical': 'False'}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('imagekit.models.fields.ProcessedImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'official_site': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'stacks': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['stack.App']", 'through': u"orm['stack.AppStack']", 'symmetrical': 'False'})
        },
        u'stack.appstack': {
            'Meta': {'object_name': 'AppStack'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'apps+'", 'to': u"orm['stack.App']"}),
            'created_at': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified_at': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'stack': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'stacks+'", 'to': u"orm['stack.App']"}),
            'used_since': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'used_until': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'})
        },
        u'stack.architecture': {
            'Meta': {'object_name': 'Architecture'},
            'app': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['stack.App']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'stack.category': {
            'Meta': {'object_name': 'Category'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'null': 'True'})
        }
    }

    complete_apps = ['stack']