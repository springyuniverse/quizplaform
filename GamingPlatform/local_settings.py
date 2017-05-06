import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'GamingPlatform',
        'USER': 'postgres',
        'PASSWORD': 'haya2008',
        'HOST': 'localhost',
        'PORT': '5454',
    }
}

DEBUG = True