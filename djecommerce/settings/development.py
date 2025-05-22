import os
from decouple import config, Csv
from .base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE

# ------------------------------------------------------------------------------
# DEBUG / HOSTS
# ------------------------------------------------------------------------------
# Turn on locally, off in production unless you explicitly set DEBUG=True
DEBUG = config('DEBUG', default=False, cast=bool)

# A comma-separated list in your env, e.g.
#   ALLOWED_HOSTS=127.0.0.1,localhost,your.azure.host
ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost',
    cast=Csv()
)

# ------------------------------------------------------------------------------
# INSTALLED APPS & MIDDLEWARE
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'debug_toolbar',
]

# prepend so the toolbar catches early middleware behaviors
MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

# ------------------------------------------------------------------------------
# django-debug-toolbar settings
# ------------------------------------------------------------------------------
DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

def show_toolbar(request):
    return DEBUG  # only show when DEBUG=True

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# ------------------------------------------------------------------------------
# DATABASE (SQLite for dev)
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, config('DEV_DB_NAME', default='db.sqlite3')),
    }
}

# ------------------------------------------------------------------------------
# Stripe keys (fallback to empty so decouple won’t explode)
# ------------------------------------------------------------------------------
STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='')
