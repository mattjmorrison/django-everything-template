from cStringIO import StringIO

from lettuce import step, world, before
from django.test.client import Client
import json

from django.db import connection
from django.core.management import call_command

from south.management.commands import patch_for_test_db_setup


@before.all
def setup_test_database():
    patch_for_test_db_setup()
    connection.creation.create_test_db(verbosity=0, autoclobber=True)


@before.each_scenario
def clean_db(scenario):
    call_command('flush', interactive=False, stderr=StringIO(), stdout=StringIO())


@step(u'Given the following data')
def given_the_following_data(step):
    step.scenario.user_data = step.hashes.first


@step(u'When I \'([^\']*)\' to the \'([^\']*)\' url')
def verb_to_url(step, verb, url):
    world.browser = Client()
    url_method = getattr(world.browser, verb.lower())
    step.scenario.response = url_method(url, step.scenario.user_data or None)


@step(u"And I '([^']*)' to the '([^']*)' url with the '([^']*)' from the previous response")
def verb_to_url_with_attribute_from_previous_response(step, verb, url, attribute):
    world.browser = Client()
    url_method = getattr(world.browser, verb.lower())
    try:
        step.scenario.latest_id = json.loads(step.scenario.response.content)[attribute]
    except:
        pass
    resource_url = url + '{}/'.format(step.scenario.latest_id)
    response = url_method(resource_url, step.scenario.user_data or None)
    step.scenario.response = response


@step("And I '([^']*)' to the '([^']*)' url with the '([^']*)' from the previous response with the following data")
def verb_to_url_with_attribute_from_previous_response_with_data(step, verb, url, attribute):
    world.browser = Client()
    url_method = getattr(world.browser, verb.lower())
    try:
        step.scenario.latest_id = json.loads(step.scenario.response.content)[attribute]
    except:
        pass
    resource_url = url + '{}/'.format(step.scenario.latest_id)
    response = url_method(resource_url, step.hashes.first)
    step.scenario.response = response


@step(u'Then I should get a \'([^\']*)\' status code')
def assert_status_code(step, status_code):
    assert status_code == str(step.scenario.response.status_code), step.scenario.response.status_code


@step(u'And I should get a valid json document in the response body')
def assert_response_body_is_valid_json(step):
    try:
        step.scenario.json_response = json.loads(step.scenario.response.content)
    except Exception as e:
        assert False, "Body was not valid json document, it was '{}' {}".format(step.scenario.response.content, e)


@step("And I should get a '([^']*)' of '([^']*)' in the json document")
def assert_json_attribute_is_value(step, attribute, value):
    expected = value
    actual = step.scenario.json_response[attribute]
    assert expected == actual, "expected {} but was {}".format(expected, actual)


@step(u'And I should see an \'([^\']*)\' field in the json document')
def assert_attribute_in_json(step, attribute):
    assert attribute in step.scenario.json_response, step.scenario.json_response
