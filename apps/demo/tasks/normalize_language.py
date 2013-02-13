from celery import task
from celery.schedules import crontab


@task(name="add")
def add(*args, **kwargs):
    print "Inside My Add Task with args: {} and kwargs: {}".format(args, kwargs)
    return "This is the return value!"


@task.periodic_task(name="tick", run_every=crontab(minute='*/1'))
def tick(*args, **kwargs):
    print "Inside my periodic task with args: {} and kwargs: {}".format(args, kwargs)
    return "This is the return value!"
