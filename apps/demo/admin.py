from django.contrib.admin import site
from apps.demo import models

site.register(models.Person)
