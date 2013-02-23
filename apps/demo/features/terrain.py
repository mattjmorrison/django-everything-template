from lettuce import world, before, after
from coverage import coverage
from django.db import connection
from django.core.management import call_command
from south.management.commands import patch_for_test_db_setup
from cStringIO import StringIO


@before.all
def prepare_coverage():
    world.cov = coverage(source=['apps'], omit=['*/features/*', '*/migrations/*', '*/tests/*'])
    world.cov.start()


@after.all
def teardown_coverage(total):
    world.cov.save()
    coverage_percent = world.cov.report()
    world.cov.stop()
    if coverage_percent < 80.0:
        raise Exception("TOTAL Coverage did not reach minimum required: 96%")


@before.all
def setup_test_database():
    patch_for_test_db_setup()
    connection.creation.create_test_db(verbosity=0, autoclobber=True)


@before.each_scenario
def clean_db(scenario):
    call_command('flush', interactive=False, stderr=StringIO(), stdout=StringIO())
