from celery import task
from celery.schedules import crontab
from apps.demo.models.person import Person
from datetime import datetime


@task.periodic_task(name="create_person", run_every=crontab(minute="*/1"))
def create_person():
    now = datetime.now().strftime("%m-%d-%Y %H:%M:%S")
    Person.objects.create(name=now, language=now)
