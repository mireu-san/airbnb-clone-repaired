from django import template

register = template.Library()

@register.filter
def mireu_capitals(value):
    return value.capitalize()