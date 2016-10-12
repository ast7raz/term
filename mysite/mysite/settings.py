"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import random
import glob
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'is*2ofnc%0i_w34%eds$##i*t#khqr&g%g9k!d7c^!4(3it3$8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',
    'books',
    "phonebook",
    "terminals",
    "calculation",
    "load_averange",
    "reestrs",

)



MIDDLEWARE_CLASSES = (
    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',


)

ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'

SESSION_EXPIRE_AT_BROWSER_CLOSE=True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "djan",
        'HOST':'localhost',
        'USER':'asorokin',
        'PASSWORD':'zaq123',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

TEMPLATE_DIRS=(
    os.path.join(BASE_DIR, "templates"),
                           )


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    )

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'

# google auth

AUTHENTICATION_BACKENDS = (
    'social.backends.google.GoogleOpenId',
    'social.backends.google.GoogleOAuth2',
    'social.backends.google.GoogleOAuth',
    'django.contrib.auth.backends.ModelBackend',
)
TEMPLATE_CONTEXT_PROCESSORS = (

    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.contrib.auth.context_processors.auth',
)
PIPELINE = (
  'social.pipeline.social_auth.social_details',
  'books.back.pick_email_valide',
  'social.pipeline.social_auth.social_uid',
  'social.pipeline.social_auth.auth_allowed',
  'social.pipeline.social_auth.social_user',
  'social.pipeline.user.get_username',
  'social.pipeline.mail.mail_validation',

  'social.pipeline.social_auth.associate_by_email',
  'social.pipeline.user.create_user',
  'social.pipeline.social_auth.associate_user',
  'social.pipeline.social_auth.load_extra_data',
  'social.pipeline.user.user_details',
)

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '206257869964-2vo10i9c9sa86nib48tvfqks0u2fm4eh.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'lHeNmZyAAXxeCmnuitCrSEvu'
