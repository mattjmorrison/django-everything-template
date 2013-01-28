from django.db import models


class Person(models.Model):
    """
    Person
    ======
        The Person model of the Demo app is to demonstrate how to change the
        plural name of the model itself as well as the string value of an
        instance.
    """
    name = models.CharField(max_length=25)
    language = models.CharField(max_length=25)

    def __unicode__(self):
        return "{} : {}".format(self.name, self.language)

    class Meta(object):
        verbose_name_plural = 'people'
        app_label = 'demo'
