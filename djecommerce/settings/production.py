from .base import *
from decouple import config

# ------------------------------------------------------------------------------
# PRODUCTION SETTINGS
# ------------------------------------------------------------------------------

DEBUG = config('DEBUG', cast=bool, default=False)

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='your-app-name.azurewebsites.net',
).split(',')

# ------------------------------------------------------------------------------
# SECURITY BEST PRACTICES
# ------------------------------------------------------------------------------
# These help prevent common security risks
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'

# ------------------------------------------------------------------------------
# DATABASE CONFIG (PostgreSQL on Azure or other)
# ------------------------------------------------------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT', default='5432'),
    }
}

# ------------------------------------------------------------------------------
# STRIPE LIVE KEYS
# ------------------------------------------------------------------------------
STRIPE_PUBLIC_KEY = config('STRIPE_LIVE_PUBLIC_KEY', default='')
STRIPE_SECRET_KEY = config('STRIPE_LIVE_SECRET_KEY', default='')

# ------------------------------------------------------------------------------
# STATIC & MEDIA FILES (Optional override for CDN or Azure Blob if needed)
# ------------------------------------------------------------------------------
# STATIC_ROOT and MEDIA_ROOT already set in base.py
# For production, ensure 'collectstatic' is run and files are served via web server or CDN
