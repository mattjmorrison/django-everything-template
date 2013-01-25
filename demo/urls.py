from django.conf.urls import patterns, include, url
from demo import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
    url(r'^$', views.Demo1.as_view()),
    url(r'^person/$', csrf_exempt(views.PersonList.as_view())),
    url(r'^person/(?P<pk>\d+)/$', csrf_exempt(views.Person.as_view())),
)
