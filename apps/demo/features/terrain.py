from lettuce import world, before, after
from coverage import coverage


@before.all
def prepare_coverage():
	world.cov = coverage(source=['apps'], omit=['*/features/*', '*/migrations/*', '*/tests/*'])
	world.cov.start()


@after.all
def teardown_browser(total):
	world.cov.save()
	coverage_percent = world.cov.report()
	world.cov.stop()
	if coverage_percent < 95.0:
		raise Exception("TOTAL Coverage did not reach minimum required: 96%")
