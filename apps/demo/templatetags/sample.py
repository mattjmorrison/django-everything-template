from django import template

register = template.Library()


@register.simple_tag(name='minustwo')
def minustwo(value):
    return value - 2
