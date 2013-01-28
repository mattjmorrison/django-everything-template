from django.contrib.admin import site
from apps.demo.models import person

site.register(person.Person)
