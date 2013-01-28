from django.conf.urls import patterns, url
from apps.demo.views import person
from apps.demo.views import demo
from django.views.decorators.csrf import csrf_exempt

urlpatterns = patterns('',
                       url(r'^$', demo.Demo1.as_view()),
                       url(r'^person/$', csrf_exempt(person.PersonList.as_view())),
                       url(r'^person/(?P<pk>\d+)/$', csrf_exempt(person.Person.as_view())),)
