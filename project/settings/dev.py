from project.settings.base import *

TEMPLATE_DEBUG = DEBUG = True
COMPRESS_ENABLED = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_ROOT, '.database'),
    }
}

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

INSTALLED_APPS = INSTALLED_APPS + (
    'debug_toolbar',
    'lettuce.django',
    'django_nose',
)

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

INTERNAL_IPS = ('127.0.0.1',)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

