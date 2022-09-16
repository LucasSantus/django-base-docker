from pathlib import Path
import os, sys

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

sys.path.append(
    os.path.join(BASE_DIR, "apps")
)

# SECRET_KEY = '0(he!754crnlnmkmat4=5^e!qg48$42dgqyn^t(brxer@-o0h#'

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = str(os.environ.get('SECRET_KEY', "django-insecure-900u2i6xbp12y#l7-%ch9h(w(jxj17n)c1btv1p=$6$iz27t7m"))

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = int(os.environ.get('DEBUG', 1))

ALLOWED_HOSTS = ['127.0.0.1', 'localhost'] # add site web

INTERNAL_IPS = ('*')

# Default Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

# Interns Apps
INSTALLED_APPS += [
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': str(os.environ.get('DB_ENGINE', 'django.db.backends.sqlite3')),
        'NAME': str(os.environ.get('DB_NAME', BASE_DIR / 'db.sqlite3')),
        'USER': str(os.environ.get('DB_USER', '')),
        'PASSWORD': str(os.environ.get('DB_PASSWORD', '')),
        'HOST': str(os.environ.get('DB_HOST', '')),
        'PORT': str(os.environ.get('DB_PORT', ''))
    }
}
# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static_files')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static")
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Redis and Celery Conf
CELERY_BROKER_URL = "redis://redis:6379"
CELERY_RESULT_BACKEND = "redis://redis:6379"
