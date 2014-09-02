
import os
from cbsettings import DjangoDefaults
from cbsettings.decorators import callable_setting


class MyDefaultSettings(DjangoDefaults):

    _apps = tuple()
    _middleware_classes = tuple()

    PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
    PROJECT_NAME = os.path.basename(PROJECT_ROOT)
    PROJECT_PATH = os.path.dirname(PROJECT_ROOT)

    # Email sending:
    EMAIL_HOST = 'localhost'
    EMAIL_PORT = '25'

    ADMINS = (
        ('default', 'vencax77@gmail.com'),
    )
    MANAGERS = ADMINS

    TIME_ZONE = 'Europe/Prague'
    LANGUAGE_CODE = 'cs'
    SITE_ID = 1
    INTERNAL_IPS = ('127.0.0.1',)
    DATETIME_FORMAT = '%d.%m.%Y %H:%M:%S'
    SHORT_DATE_FORMAT = 'd.m. y'
    DEFAULT_STATE_CODE = 'CZE'

    LOGIN_REDIRECT_URL = '/'

    USE_I18N = True
    USE_L10N = True

    ROOT_URLCONF = '%s.urls' % PROJECT_NAME

    MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media') + '/'
    MEDIA_URL = '/media/'

    STATIC_ROOT = os.path.join(PROJECT_PATH, 'static') + '/'
    STATIC_URL = '/static/'

    STATICFILES_DIRS = (
      os.path.join(PROJECT_ROOT, 'static'),
    )

    STATICFILES_FINDERS = (
        'django.contrib.staticfiles.finders.FileSystemFinder',
        'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

    SECRET_KEY = os.environ['DJANGO_SECRET']

    TEMPLATE_LOADERS = (
      'django.template.loaders.filesystem.Loader',
      'django.template.loaders.app_directories.Loader',
    )
    TEMPLATE_DIRS = ('%s/templates' % PROJECT_ROOT,)

    LOCALE_PATHS = (os.path.join(PROJECT_ROOT, 'locale'), )

    @callable_setting
    def add_app(self, app):
        """
        Insert an application into application set.
        Try to initialize the app and load required stuff.
        """
        if app not in self._apps:
            self._apps += (app,)

    @callable_setting
    def add_apps(self, apps):
        for a in apps:
            self.add_app(a)

    @callable_setting
    def add_middleware(self, middleware):
        if middleware not in self._middleware_classes:
            self._middleware_classes += (middleware,)

    @callable_setting
    def add_middlewares(self, middlewares):
        for m in middlewares:
            self.add_middleware(m)

    @property
    def MIDDLEWARE_CLASSES(self):
        return tuple(self._middleware_classes)

    @property
    def INSTALLED_APPS(self):
        return tuple(self._apps)

#    @property
#    def ABSOLUTE_URL_OVERRIDES(self):
#        if not hasattr(self, '_fcms_settings'):
#            from vxkcms.utils import collect_fcms_settings
#            self._fcms_settings = collect_fcms_settings(self._apps)
#        return self._fcms_settings['url_overrides']

    @property
    def SOUTH_MIGRATION_MODULES(self):
        retval = {}
        for a in self.INSTALLED_APPS:
            if a == 'south' or 'django.contrib' in a:
                continue
            applabel = a.split('.')[-1]
            retval[applabel] = 'migrate.%s' % applabel
        return retval
