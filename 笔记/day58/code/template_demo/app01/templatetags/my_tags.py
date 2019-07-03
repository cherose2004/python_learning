from django import template

register = template.Library()
from django.utils.safestring import mark_safe


@register.filter
def add_xx(value, arg):  # 最多有两个

    return '{}-{}'.format(value, arg)


@register.filter
def multiply(value, arg):  # 最多有两个

    return value * arg


@register.filter()
def show_a(url, name):  # 最多有两个

    return mark_safe('<a href="{}">{}</a>'.format(url, name))


@register.simple_tag
def join_str(*args, **kwargs):
    return '{} - {} '.format('*'.join(args), '$'.join(kwargs.values()))


