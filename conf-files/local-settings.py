import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

ADMINS = (
        ('Seshagiri Prabhu', 'seshagiriprabhu@gmail.com'),
        ('Hari Raghavendra', 'raghu.rathode@gmail.com'),
)

ADMINS_EMAIL = map(lambda x: x[1], ADMINS)

MANAGERS = ADMINS

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = []

SECRET_KEY = 'zhn*c572ve296o$a822a&hmf_5+ot(q-dp+9&56ep7jdtx4(rt'

TEMPLATE_DIRS = (
    BASE_DIR + "/templates",
)

TIME_ZONE = 'UTC'

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'communityapp',
        'USER': 'postgres',
        'PASSWORD': 'blob',
        'HOST': 'localhost',
        'PORT': '',
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
