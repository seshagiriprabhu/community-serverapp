import os
import sys
sys.path.append('/usr/local/django')
sys.path.append('/var/www')
sys.path.append('/var/www/community-serverapp')
sys.path.append('/var/www/community-serverapp/media')
os.environ['DJANGO_SETTINGS_MODULE'] = 'communityapp.settings'

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

path = '/var/www/community-serverapp'
if path not in sys.path:
    sys.path.append(path)
