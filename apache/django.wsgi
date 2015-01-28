import os
import sys
sys.path.append('/usr/local/django')
sys.path.append('/var/www')
sys.path.append('/var/www/community-serverapp')
sys.path.append('/var/www/community-serverapp/media')
os.environ['DJANGO_SETTINGS_MODULE'] = 'community-serverapp.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

path = '/var/www/community-serverapp'
if path not in sys.path:
    sys.path.append(path)
