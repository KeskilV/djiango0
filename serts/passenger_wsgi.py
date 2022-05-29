# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1689804/data/www/ygemlab.ru/ygemlabru')
sys.path.insert(1, '/var/www/u1689804/data/djangoenv/lib/python10.1/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'ygemlabru.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()