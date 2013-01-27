from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^restframework', include('rest_framework.urls', namespace='djangorestframework')),
                       url(r'^demo/', include('apps.demo.urls')),)
