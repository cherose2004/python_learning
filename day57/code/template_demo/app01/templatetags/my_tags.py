from django import template

register = template.Library()


@register.filter
def add_xx(value, arg):  # 最多有两个

    return '{}-{}'.format(value, arg)
