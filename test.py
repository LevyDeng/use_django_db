import os,django
from django.conf import  settings

os.environ['DJANGO_SETTINGS_MODULE']="D:\work\Pycharm\use_django_db\use_django_db\settings.py"
if not settings.configured:
    settings.configure()

print os.environ['DJANGO_SETTINGS_MODULE']
print settings.configured