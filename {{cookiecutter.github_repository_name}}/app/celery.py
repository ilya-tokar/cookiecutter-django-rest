import os

from celery import Celery
from celery.schedules import crontab

timezone = 'Europe/Moscow'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spels_test_work_backend.settings')

app = Celery('spels_test_work_backend')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    # Executes every Monday morning at 7:30 a.m.
    'add-every-monday-morning': {
        'task': 'tasker.tasks.update',
        'schedule': crontab(minute='*/2'),
        'args': (16, 16),
    },
}
