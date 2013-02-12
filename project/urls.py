from django.conf.urls import patterns, include, url
from django.contrib import admin
from apps.demo.tasks import normalize_language
admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^restframework', include('rest_framework.urls', namespace='djangorestframework')),
                       url(r'^demo/', include('apps.demo.urls')),)
