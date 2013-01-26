from project.settings.base import *

TEMPLATE_DEBUG = DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, '.production_database'),
    }
}

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True