from rest_framework import generics
from apps.demo.models import person


class PersonList(generics.ListCreateAPIView):
    model = person.Person


class Person(generics.RetrieveUpdateDestroyAPIView):
    model = person.Person
