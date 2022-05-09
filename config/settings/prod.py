from .base import *
from dotenv import load_dotenv


load_dotenv()
DEBUG = False

SECRET_KEY = os.environ.get("SECRET_KEY")


ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'humanscape',
        'USER': os.environ.get("ROOT"),
        'PASSWORD': os.environ.get("MYSQL_LOCAL_PASSWORD"),
        'HOST': os.environ.get("HOST"),
        'PORT': os.environ.get("PORT")
    }
}