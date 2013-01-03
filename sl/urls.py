from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^stack/', include('stack.urls')),
    url(r'^$', TemplateView.as_view(template_name='index.html')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
