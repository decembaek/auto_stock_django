"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
import os
import pymysql

pymysql.install_as_MySQLdb()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-1f@%2r435^7tjq*ajzr12=$dnt3^!t&1tu5w4(ed=jlyt#3ur5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

THIRD_PARTY_APPS = [
    "rest_framework",
    # pip install django-extensions
    # Django-extensions를 이용해 DB ERD, 엔티티 만들기
    "django_extensions",
]

CUSTOM_APPS = [
    "korea_stock.apps.KoreaStockConfig",
    "common.apps.CommonConfig",
    "users.apps.UsersConfig",
    "mock_invest.apps.MockInvestConfig",
    "tournament.apps.TournamentConfig",
]

SYSTEM_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
INSTALLED_APPS = SYSTEM_APPS + THIRD_PARTY_APPS + CUSTOM_APPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

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

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

from dotenv import load_dotenv

load_dotenv()

HOST = os.environ.get("HOST")
# NAME = os.environ.get("NAME")
# USER = os.environ.get("USER")
PASSWORD = os.environ.get("PASSWORD")
DOCKER_PASSWORD = os.environ.get("DOCKER_PASSWORD")

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "aws_stock_match",
        "USER": "root",
        "PASSWORD": DOCKER_PASSWORD,
        "HOST": "127.0.0.1",
        "PORT": "13306",
    },
    "docker_mysql": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "aws_stock_match",
        "USER": "root",
        "PASSWORD": DOCKER_PASSWORD,
        "HOST": "127.0.0.1",
        "PORT": "13306",
    },
    "aws_mysql": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "aws_stock",
        "USER": "admin",
        "PASSWORD": PASSWORD,
        "HOST": HOST,
        "PORT": "3306",
    },
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": "aws_stock",
#         "USER": "admin",
#         "PASSWORD": PASSWORD,
#         "HOST": HOST,
#         "PORT": "3306",
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

# LANGUAGE_CODE = "en-us"

# TIME_ZONE = "UTC"
LANGUAGE_CODE = "ko-kr"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# Django-extensions를 이용해 DB ERD, 엔티티 만들기
GRAPH_MODELS = {
    "all_applications": True,
    "group_models": True,
}
# Celery가 장고 프로젝트를 자동으로 인식할 수 있도록 설정합니다.
CELERY_IMPORTS = [
    "korea_stock.tasks",
]
# Auth 사용자 유저 커스텀
AUTH_USER_MODEL = "users.User"
# settings.py
CELERY_BROKER_URL = "redis://localhost:6379/0"  # Redis를 사용하는 경우
