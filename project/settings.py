import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY', "django-insecure-s17vk&5n62vk&mnsaxvgh&nkmv#fie42$1k$(j1x53#wulnv$n")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'borja-relecloud-drhhfffnbbhcb0hf.spaincentral-01.azurewebsites.net',  
    '127.0.0.1',
    'localhost'
]


# Static files storage
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap4',
    'relecloud.apps.RelecloudConfig',
    'whitenoise.runserver_nostatic'
]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# CSRF Trusted Origins
CSRF_TRUSTED_ORIGINS = [
    'https://borja-relecloud-drhhfffnbbhcb0hf.spaincentral-01.azurewebsites.net',
    'http://borja-relecloud-drhhfffnbbhcb0hf.spaincentral-01.azurewebsites.net',
]

# Middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "project.wsgi.application"


# Database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",
        "USER": "adminrelecloud",
        "PASSWORD": "Libert@d25", 
        "HOST": "postgresql-relecloud.postgres.database.azure.com",
        "PORT": "5432",
        "OPTIONS": {
            "sslmode": "require"
        }
    }
}



# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
STATIC_ROOT = BASE_DIR / 'staticfiles'


# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# # HTTPS and Security Settings
SECURE_SSL_REDIRECT = False
SECURE_HSTS_SECONDS = 31536000  # Fuerza HSTS por 1 año
SECURE_HSTS_INCLUDE_SUBDOMAINS = True  # Aplica HSTS a todos los subdominios
SECURE_HSTS_PRELOAD = True  # Permite que tu dominio se incluya en la lista HSTS Preload
SECURE_REFERRER_POLICY = "strict-origin-when-cross-origin"  # Política de referencias
SECURE_BROWSER_XSS_FILTER = True  # Protege contra ataques XSS
SECURE_CONTENT_TYPE_NOSNIFF = True  # Protege contra el tipo de contenido no seguro
# CSRF_COOKIE_SECURE = True  # Las cookies CSRF solo se envían a través de HTTPS
# SESSION_COOKIE_SECURE = True  # Las cookies de sesión solo se envían a través de HTTPS

# # Email settings
# DEFAULT_FROM_EMAIL = '9205113@alumnos.ufv.es'
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.office365.com'
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True
# EMAIL_HOST_USER = DEFAULT_FROM_EMAIL
# EMAIL_HOST_PASSWORD = ''