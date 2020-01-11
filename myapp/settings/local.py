from .base import *
import os
DEBUG = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'NAME': 'my_database',
        'USER': 'root',
        'PASSWORD': 'password',
    }
}