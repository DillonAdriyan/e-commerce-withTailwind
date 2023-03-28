"""
Django settings for mystore project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config('SECRET_KEY',cast=str, default='CHANGEME!!!')


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG',cast=str,default=True)

ALLOWED_HOSTS = ['*']

CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS',cast=str,default='http://localhost:8000 http://127.0.0.1:8000').split(' ')

# Application definition
INSTALLED_APPS = [
    #base
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'livereload',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.gis',
    "debug_toolbar",
    
    #3rd party
    'hitcount',
    'rest_framework',
    'rest_framework.authtoken',
    'social_django',
    'heroicons',
    'import_export',
    'modelcluster',
    'taggit',
    'fontawesomefree',
    # 'cities',

    #my apps
    'accounts',
    'saleproduct',
    'carts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'mystore.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
                'saleproduct.context_processors.get_info'
            ],
        },
    },
]

WSGI_APPLICATION = 'mystore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('DATABASE_ENGI',cast=str,default='django.db.backends.postgresql_psycopg2'),
        'NAME': config('DATABASE_NAME',cast=str,default='saleapp'),
        'HOST': config('DATABASE_HOST',cast=str,default='localhost'),
        'PORT': config('DATABASE_PORT',cast=str,default='5432'),
        'USER': config('DATABASE_USER',cast=str,default='postgres'),
        'PASSWORD': config('DATABASE_PASSWORD',cast=str,default='postgres'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/


LANGUAGE_CODE = 'vi'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_L10N = True

USE_TZ = True


LANGUAGES = [
    ('vi', _('Vietnamese')),
    ('en', _('English')),
]

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static/'),
]

STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

BASE_URL = config('BASE_URL', default='http://localhost:8000')

SOCIAL_AUTH_JSONFIELD_ENABLED = True

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
]


SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = config('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY',default='',cast=str)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = config('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET',default='',cast=str)
SOCIAL_AUTH_GOOGLE_OAUTH2_WHITELISTED_DOMAINS = ['gmail.com']

CSRF_TRUSTED_ORIGIN = config('TRUSTED_ORIGIN',default='',cast=str)
CORS_TRUSTED_ORIGIN = config('TRUSTED_ORIGIN',default='',cast=str)

USE_THOUSAND_SEPARATOR = True

AUTH_USER_MODEL = 'accounts.CustomUserAccount'

CITIES_DATA_DIR = os.path.join(BASE_DIR, 'cities_data')

CITIES_FILES = {
    # ...
    'city': {
       'filename': 'VN.zip',
       'urls':['http://download.geonames.org/export/dump/'+'{filename}']
    },
    # ...
}
CITIES_POSTAL_CODES = ['VN']

SITE_NAME = config('SITENAME',default='ZEN Store',cast=str)
SHOP_NAME = config('SHOPNAME',default='ZEN Store',cast=str)
SHOP_ADDRESS = config('SHOPADDRESS',default='Hà Nội',cast=str)
SHOP_PHONE = config('SHOPPHONE',default='0123456789',cast=str)
SHOP_EMAIL = config('SHOPEMAIL',default='',cast=str)
SHOP_FACEBOOK = config('SHOP_FACEBOOK',default='',cast=str)
SHOP_INSTAGRAM = config('SHOP_INSTAGRAM',default='',cast=str)
SHOP_ZALO = config('SHOP_ZALO',default='',cast=str)
SHOP_TIKTOK = config('SHOP_TIKTOK',default='',cast=str)

if DEBUG:
    import socket  # only if you haven't already imported this
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

HITCOUNT_KEEP_HIT_ACTIVE = { 'hours': 0.5 }

HITCOUNT_HITS_PER_IP_LIMIT = 1


CART_SESSION_ID = config('CART_SESSION_ID',default='cart',cast=str)

EMAIL_MASTER = config('EMAIL_MASTER',default=f'noreply@{BASE_URL}',cast=str)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

PAGINATE_BY = config('PAGINATE_BY',default=10,cast=int)

# VNPAY CONFIG
VNPAY_RETURN_URL = config('VNPAY_RETURN_URL',default='http://localhost:8000/payment/return',cast=str)
VNPAY_PAYMENT_URL = config('VNPAY_PAYMENT_URL',default='https://sandbox.vnpayment.vn/paymentv2/vpcpay.html',cast=str)
VNPAY_API_URL = config('VNPAY_API_URL',default='https://sandbox.vnpayment.vn/merchant_webapi/merchant.html',cast=str) 
VNPAY_TMN_CODE = config('VNPAY_TMN_CODE',default='',cast=str) # Merchant code, get from config
VNPAY_HASH_SECRET_KEY = config('VNPAY_HASH_SECRET_KEY',default='',cast=str) # Hash secret key, get from config