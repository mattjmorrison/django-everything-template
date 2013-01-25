import unittest
from demo import models


class PersonModelTests(unittest.TestCase):
    
    def test_user_unicode_resturns_name_and_language(self):
        person = models.Person(name='Steve', language='Python')
        self.assertEqual(u"Steve : Python", unicode(person))

    def test_plural_name_is_correct(self):
        self.assertEqual('people', models.Person._meta.verbose_name_plural)
