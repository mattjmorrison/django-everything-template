from celery import task

@task(name="add")
def add(*args, **kwargs):
    print "Inside My Add Task with args: {} and kwargs: {}".format(args, kwargs)
    return "This is the return value!"
