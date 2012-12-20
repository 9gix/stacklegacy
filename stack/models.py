from django.db import models

class App(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    official_site = models.URLField()
    stacks = models.ManyToManyField('self', through='AppStack',
            symmetrical=False)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __unicode__(self):
        return self.name

class AppStack(models.Model):
    app = models.ForeignKey('App', related_name="apps+")
    stack = models.ForeignKey('App', related_name="stacks+")
    category = models.ForeignKey('Category', blank=True, null=True)
    description = models.TextField()
    used_since = models.DateField(blank=True, null=True)
    used_until = models.DateField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return "%(app)s Stack (%(category)s: %(stack)s)" % \
                {'app':self.app,
                'category':self.category,
                'stack':self.stack}
