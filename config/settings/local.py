import os
import pymysql
from dotenv import load_dotenv

from .base import *

load_dotenv()

DEBUG = True

SECRET_KEY = os.environ.get("SECRET_KEY"),

ALLOWED_HOSTS = ['*']


pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'humanscape',
        'USER': 'root',
        'PASSWORD': os.environ.get("MYSQL_LOCAL_PASSWORD"),
        'HOST': 'localhost',
        'PORT': 3306
    }
}

'''
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
'''