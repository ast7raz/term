import os, sys, subprocess

sys.stdout = sys.stderr
sys.path.append('/var/www-support/mysite')
sys.path.append('/usr/local/lib/python2.7/Lib/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()