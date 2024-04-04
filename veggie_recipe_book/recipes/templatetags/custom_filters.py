from django import template

register = template.Library()


@register.filter(name='split_newline')
def split_newline(value):
    return value.split('\n')
