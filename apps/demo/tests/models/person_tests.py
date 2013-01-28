import unittest
from apps.demo.models import person


class PersonModelTests(unittest.TestCase):

    def test_user_unicode_resturns_name_and_language(self):
        sut = person.Person(name='Steve', language='Python')
        self.assertEqual(u"Steve : Python", unicode(sut))

    def test_plural_name_is_correct(self):
        self.assertEqual('people', person.Person._meta.verbose_name_plural)
