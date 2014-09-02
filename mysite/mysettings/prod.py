
import os
from .common import MyCommonSettings


class MyProductionSettings(MyCommonSettings):
    DEBUG = False
    TEMPLATE_DEBUG = SERVE_STATICS = False
    DEBUG_TOOLBAR = False

    DATABASES = {
            'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pginadb',
            'USER': os.environ['DBUSER'],
            'PASSWORD': os.environ['DBPASS'],
            'HOST': 'localhost',
            'PORT': '3306'
        }
    }

    def __init__(self):
        super(MyProductionSettings, self).__init__()

        self.add_middleware('django.middleware.cache.CacheMiddleware')
