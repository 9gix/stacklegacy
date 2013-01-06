from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors.resize import ResizeToFit
from django.contrib.contenttypes import generic
from ref.models import Reference

class Architecture(models.Model):
    app = models.ForeignKey('App')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    references = generic.GenericRelation(Reference)

class App(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(blank=True)
    logo = ProcessedImageField(processors=[ResizeToFit(200,200)],
            upload_to='logo', null=True, blank=True,
            format='JPEG', options={'quality':90})
    slug = models.SlugField(unique=True)
    official_site = models.URLField(null=True, blank=True)
    stacks = models.ManyToManyField('self', through='AppStack',
            symmetrical=False)

    categories = models.ManyToManyField('Category')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

class AppStack(models.Model):
    app = models.ForeignKey('App', related_name="apps+")
    stack = models.ForeignKey('App', related_name="stacks+")
    description = models.TextField(blank=True)
    used_since = models.DateField(blank=True, null=True)
    used_until = models.DateField(blank=True, null=True)
    references = generic.GenericRelation(Reference)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%(app)s Stack (%(category)s: %(stack)s)" % \
                {'app':self.app,
                'category':self.category,
                'stack':self.stack}
