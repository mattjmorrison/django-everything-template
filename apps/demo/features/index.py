# -*- coding: utf-8 -*-
from lettuce import step, world
from django.test.client import Client
from BeautifulSoup import BeautifulSoup


@step(u'Given I am on the url \'([^\']*)\'')
def given_i_am_on_the_url_group1(step, url):
    world.browser = Client()
    step.scenario.response = world.browser.get(url)


@step(u'When I get look at the \'([^\']*)\' field')
def when_i_get_look_at_the_group1_field(step, field):
    soup = BeautifulSoup(step.scenario.response.content)
    step.scenario.value = soup.find('div', {'id': field}).text


@step(u'Then I should see \'([^\']*)\'')
def then_i_should_see_group1(step, value):
    assert step.scenario.value == value, "{} != {}".format(step.scenario.value, value)
