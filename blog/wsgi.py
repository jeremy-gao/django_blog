import os,sys
from os.path import join,dirname,abspath
from django.core.wsgi import get_wsgi_application

PROJECT_DIR = dirname(dirname(abspath(__file__)));
sys.path.insert(0,PROJECT_DIR);
os.environ["DJANGO_SETTINGS_MODULE"] = "website.settings";
application = get_wsgi_application();
