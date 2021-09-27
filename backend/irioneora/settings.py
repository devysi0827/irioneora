"""
Django settings for irioneora project.

Generated by 'django-admin startproject' using Django 3.2.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path


from . import mysql_settings

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-u(+tceq^_7a$*$jy&ia)=$p3k@yfa3os1)r#eu)^c_@%kz4rgi'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# ALLOWED_HOSTS = ['j5a601.p.ssafy.io',
#                  'localhost',
#                  'localhost:8080/',
#                  '127.0.0.1']
CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # allauth

    # django apps
    'pages',
    'accounts',
    'artifacts',

    # 3rd party apps
    'drf_yasg',  # for swagger
    'rest_framework',
    'rest_framework.authtoken',
    'rest_auth',
    'rest_auth.registration',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.kakao',
    'django_extensions',
    # cors
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'irioneora.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'irioneora.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = mysql_settings.DATABASES


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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

'''
vvvvv accounts settings vvvvv 
'''

AUTH_USER_MODEL = 'accounts.User'

# rest-auth signup serializer
# 회원가입 시리얼라이저 커스텀
REST_AUTH_REGISTER_SERIALIZERS = {
    'REGISTER_SERIALIZER': 'accounts.serializers.CustomRegisterSerializer',
}

# 프로필페이지
REST_AUTH_SERIALIZERS = {
    # rest-auth/user/
    'USER_DETAILS_SERIALIZER': 'accounts.serializers.CustomUserDetailSerializer',
    'LOGIN_SERIALIZER': 'accounts.serializers.CustomLoginSerializer',
}



# 시리얼라이저에서 보낸 정보 저장
ACCOUNT_ADAPTER = 'accounts.adapter.CustomAccountAdapter'

# DRF setting
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',  # DRF-Token
    ]
}

# django.contrib.sites 에서 사용
SITE_ID = 1

'''
^^^^^ accounts settings ^^^^^ 
'''
