from django.conf.urls import patterns, url, include
from stack.views import StackListView, StackDetailView

from tastypie.api import Api
from stack.api import AppResource, AppStackResource, StackResource, ReferenceResource, ArchitectureResource

v1_api = Api(api_name='v1')
v1_api.register(AppResource())
v1_api.register(AppStackResource())
v1_api.register(StackResource())
v1_api.register(ReferenceResource())
v1_api.register(ArchitectureResource())


urlpatterns = patterns('',
        (r'^api/', include(v1_api.urls)),
        (r'^(?P<pk>\d+)/$', StackDetailView.as_view()),
        (r'^$', StackListView.as_view()),
)
