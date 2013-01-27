import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings.deployed")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
