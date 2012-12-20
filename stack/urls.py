from django.conf.urls import patterns, url, include
from stack.views import StackListView, StackDetailView

from tastypie.api import Api
from stack.api import AppResource, AppStackResource

v1_api = Api(api_name='v1')
v1_api.register(AppResource())
v1_api.register(AppStackResource())


urlpatterns = patterns('',
        (r'^api/', include(v1_api.urls)),
        (r'^(?P<pk>\d+)/$', StackDetailView.as_view()),
        (r'^$', StackListView.as_view()),
)
