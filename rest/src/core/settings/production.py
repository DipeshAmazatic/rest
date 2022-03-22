"""
Django local settings template for core project
"""


import os
from pathlib import Path
import dj_database_url
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True #if (os.environ.get("DEBUG", "true").lower() == "true") else False

ALLOWED_HOSTS = ['restdemoproject.herokuapp.com/','127.0.0.1',]

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DEFAULT_CONNECTION = dj_database_url.parse(os.environ.get('DATABASE_URL'))
DEFAULT_CONNECTION.update({"CONN_MAX_AGE": 600})
DATABASES = {"default": DEFAULT_CONNECTION}


## send email using smtp ##

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_USE_TLS = True if (os.environ.get("EMAIL_USE_TLS", "true").lower() == "true") else False
#EMAIL_USE_SSL = True if (os.environ.get("EMAIL_USE_SSL", "true").lower() == "true") else False
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')


