
from .default import MyDefaultSettings

installed_apps = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.admin',
    
    'south',
    'nss_admin',
#    'samba_admin',
#    'dhcp_admin',
#    'building_admin',
#    'school_sched',
#    'schoolagenda',
)

class MyCommonSettings(MyDefaultSettings):
    
    DEFAULT_FROM_EMAIL = 'admin@skola.local'
    
    LANGUAGES = (
      ('cs', 'Czech'),
    )
    
    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
    )
    
    TEMPLATE_CONTEXT_PROCESSORS = (
        'django.contrib.auth.context_processors.auth',
        'django.core.context_processors.i18n',
        'django.core.context_processors.request',
        'django.core.context_processors.media',
        'django.core.context_processors.static',
        'django.contrib.messages.context_processors.messages',
    )
    
    HASH_METHOD = 'CRYPT'
    PGINA_HACKS = True
    HOMES_PATH = '/samba/homes'
    DEFAULT_SHELL = '/bin/bash'
    DELETE_HOME_ON_DELETION = True
    ISSUE_SAMBA_COMMANDS = True

    def __init__(self):
        super(MyCommonSettings, self).__init__()
        
        self.add_apps(installed_apps)
        
        self.add_middlewares((
            'django.middleware.common.CommonMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.locale.LocaleMiddleware',
            'django.middleware.transaction.TransactionMiddleware',
        ))
    
    