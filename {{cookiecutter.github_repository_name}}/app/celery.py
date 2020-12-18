import os

from celery import Celery
from celery.schedules import crontab

timezone = 'Europe/Moscow'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'print_hello_console': {
        'task': 'tasker.tasks.hello',
        'schedule': crontab(minute='*/2'),
        'args': (16, 16),
    },
}
