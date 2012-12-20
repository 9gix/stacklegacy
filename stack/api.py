from tastypie.resources import Resource, ModelResource
from tastypie import fields
from stack.models import App, AppStack

class AppResource(ModelResource):
    stacks = fields.ToManyField('stack.api.AppStackResource',
            attribute=lambda bundle: bundle.obj.stacks.through.objects.filter(
                app=bundle.obj) or bundle.obj.stacks, full=True)
    class Meta:
        queryset = App.objects.all()


class AppStackResource(ModelResource):
    stack = fields.ToOneField(AppResource, 'stack')

    class Meta:
        queryset = AppStack.objects.all()
