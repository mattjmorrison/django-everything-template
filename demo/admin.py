from django.contrib.admin import site
from demo import models

site.register(models.Person)