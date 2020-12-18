from spels_test_work_backend.celery import app
from .parser.parser_scopus import ParserScopus
from author.models import AuthorModels
from publications.models import PublicationModelScopus
from celery.schedules import crontab
from datetime import timedelta


@app.task
def hello(*args, **kwargs):
    """ this task print hello on console """
    print('hello')
