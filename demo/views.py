from django.views.generic import TemplateView
from rest_framework import generics
from . import models


class Demo1(TemplateView):
    template_name = 'demo/demo1.html'


class PersonList(generics.ListCreateAPIView):
    model = models.Person


class Person(generics.RetrieveUpdateDestroyAPIView):
    model = models.Person
