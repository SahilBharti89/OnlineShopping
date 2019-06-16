import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE','OnlineShopping.settings')

app = Celery('OnlineShopping')

app.config_from_object('django.conf:settings',namespace='CELERY')
app.autodiscover_tasks()
