from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings
from pytz import timezone


BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')


os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
app = Celery('core')
app.conf.enable_utc = False
app.conf.update(timezone='Asia/Dhaka')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
app.conf.broker_url = BASE_REDIS_URL



@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')