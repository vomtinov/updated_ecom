from .base import *
from decouple import config

# ---------------------------------------------------------------------
# PRODUCTION ENVIRONMENT CONFIGURATION
# ---------------------------------------------------------------------
DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='your-app-name.azurewebsites.net',
).split(',')

# ---------------------------------------------------------------------
# SECURITY SETTINGS
# ---------------------------------------------------------------------
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# ---------------------------------------------------------------------
# DATABASE CONFIGURATION (PostgreSQL or fallback)
# ---------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME', default='db'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# ---------------------------------------------------------------------
# STRIPE KEYS (Live mode)
# ---------------------------------------------------------------------
STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY', default='')

# ---------------------------------------------------------------------
# STATIC FILES (Ensure STATIC_URL is set in base.py)
# ---------------------------------------------------------------------
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'
