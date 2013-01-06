from tastypie.resources import Resource, ModelResource, ALL
from tastypie import fields
from tastypie.utils import trailing_slash
from stack.models import App, AppStack, Architecture, Category
from django.conf.urls import url
from django.core.paginator import Paginator, InvalidPage
from haystack.query import SearchQuerySet

class SystemResource(ModelResource):
    class Meta:
        queryset = App.objects.all()
        ordering = ['modified_at', 'created_at']
        fields = ['name', 'description', 'slug', 'modified_at','logo', 'created_at']
        include_resource_uri = False

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/search%s$" % (
                    self._meta.resource_name, trailing_slash()),
                self.wrap_view('get_search'),
                name="api_get_search"),
        ]

    def get_search(self, request, **kwargs):
        self.method_check(request, allowed=['get'])
        self.is_authenticated(request)
        self.throttle_check(request)

        sqs = SearchQuerySet().models(App).load_all().auto_query(request.GET.get('q',''))
        paginator = Paginator(sqs, 20)

        try:
            page = paginator.page(int(request.GET.get('page', 1)))
        except InvalidPage:
            raise Http404("No Result Found")

        objects = []
        for result in page.object_list:
            bundle = self.build_bundle(obj=result.object, request=request)
            bundle = self.full_dehydrate(bundle)
            objects.append(bundle)

        object_list = {
            'objects': objects,
        }

        self.log_throttled_access(request)
        return self.create_response(request, object_list)


class ArchitectureResource(ModelResource):
    references = fields.ToManyField('stack.api.ReferenceResource', 'references', null=True, full=True)

    class Meta:
        queryset = Architecture.objects.all()


class AppResource(ModelResource):
    stacks = fields.ToManyField('stack.api.AppStackResource',
            attribute=lambda bundle: bundle.obj.stacks.through.objects.filter(
                app=bundle.obj), full=True, null=True)
    architectures = fields.ToManyField('stack.api.ArchitectureResource', lambda bundle: Architecture.objects.filter(app=bundle.obj), null=True, full=True)
    class Meta:
        queryset = App.objects.all()
        ordering = ['modified_at', 'created_at', 'name']

    def prepend_urls(self):
        return [
            url(r"^(?P<resource_name>%s)/(?P<slug>[\w\d_.-]+)%s$" % (
                    self._meta.resource_name, trailing_slash()),
                self.wrap_view('dispatch_detail'),
                name="api_dispatch_detail"),
        ]


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

class CategoryResource(ModelResource):

    class Meta:
        queryset = Category.objects.exclude(app=None)

from tastypie.contrib.contenttypes.fields import GenericForeignKeyField
from ref.models import Reference


class ReferenceResource(ModelResource):

    class Meta:
        resource_name = 'reference'
        queryset = Reference.objects.all()
        fields = ['url']
        include_resource_uri = False
