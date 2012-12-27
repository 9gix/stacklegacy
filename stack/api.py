from tastypie.resources import Resource, ModelResource, ALL
from tastypie import fields
from stack.models import App, AppStack
from django.conf.urls import url

class AppResource(ModelResource):
    stacks = fields.ToManyField('stack.api.AppStackResource',
            attribute=lambda bundle: bundle.obj.stacks.through.objects.filter(
                app=bundle.obj), full=True, null=True)
    references = fields.ToManyField('stack.api.ReferenceResource', 'references', null=True, full=True)
    class Meta:
        queryset = App.objects.all()

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<slug>[\w\d_.-]+)/$" %\
                    self._meta.resource_name,
                    self.wrap_view('dispatch_detail'),
                    name="api_dispatch_detail"),]

class AppStackResource(ModelResource):
    stack = fields.ToOneField(AppResource, 'stack', full=True, max_depth=2)
    references = fields.ToManyField('stack.api.ReferenceResource', 'references', null=True, full=True)

    class Meta:
        queryset = AppStack.objects.all()

class StackResource(ModelResource):
    stacks = fields.ToManyField('self',
            attribute=lambda bundle: bundle.obj.stacks.all(), full=True, null=True )

    class Meta:
        queryset = App.objects.all()

from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from ref.models import Reference

class ReferenceResource(ModelResource):

    class Meta:
        resource_name = 'reference'
        queryset = Reference.objects.all()
        fields = ['url']
        include_resource_uri = False
