from project.settings.base import *  # NOQA

TEMPLATE_DEBUG = DEBUG = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'production_djeverything',
        'HOST': 'localhost',
        'USER': 'postgres',
        'PASSWORD': 'testing',
    }
}

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = True
