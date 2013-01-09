from django.conf.urls import patterns, url, include
from stack.views import StackListView, StackUpdate, StackCreate, StackDelete

from tastypie.api import Api
from stack.api import AppResource, AppStackResource, StackResource, ReferenceResource, ArchitectureResource, SystemResource, CategoryResource

v1_api = Api(api_name='v1')
v1_api.register(AppResource())
v1_api.register(AppStackResource())
v1_api.register(StackResource())
v1_api.register(ReferenceResource())
v1_api.register(ArchitectureResource())
v1_api.register(SystemResource())
v1_api.register(CategoryResource())


urlpatterns = patterns('',
    (r'^api/', include(v1_api.urls)),
    url(r'^delete/(?P<slug>[-_\w]+)/$', StackDelete.as_view(),
        name='stack-delete'),
    url(r'^edit/(?P<slug>[-_\w]+)/$', StackUpdate.as_view(),
        name='stack-update'),
    url(r'^add/$', StackCreate.as_view(),
        name='stack-create'),
    url(r'^$', StackListView.as_view(), name='stack-list'),
)
