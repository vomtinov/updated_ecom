import os
from decouple import config, Csv
from .base import BASE_DIR, INSTALLED_APPS, MIDDLEWARE

# ------------------------------------------------------------------------------
# DEBUG & HOST CONFIG
# ------------------------------------------------------------------------------
DEBUG = config('DEBUG', default=True, cast=bool)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='127.0.0.1,localhost',
    cast=Csv()
)

# In Azure, make sure to set:
# ALLOWED_HOSTS=your-app-name.azurewebsites.net,127.0.0.1,localhost

# ------------------------------------------------------------------------------
# INSTALLED APPS & MIDDLEWARE
# ------------------------------------------------------------------------------
INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + MIDDLEWARE

# ------------------------------------------------------------------------------
# DEBUG TOOLBAR
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
    return DEBUG  # Only show if DEBUG is on

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# ------------------------------------------------------------------------------
# SQLITE DB FOR LOCAL DEVELOPMENT
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, config('DEV_DB_NAME', default='db.sqlite3')),
    }
}

# ------------------------------------------------------------------------------
# STRIPE KEYS (read from environment, fallback to empty string)
# ------------------------------------------------------------------------------
STRIPE_PUBLIC_KEY = config('STRIPE_TEST_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_TEST_SECRET_KEY', default='')

# ------------------------------------------------------------------------------
# STATIC FILES STORAGE FIX (Optional here, already in base.py is enough)
# ------------------------------------------------------------------------------
# You can override STATICFILES_STORAGE here too if needed.
