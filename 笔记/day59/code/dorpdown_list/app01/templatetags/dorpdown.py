from django.template import Library

register = Library()


@register.inclusion_tag('dropdown_list.html')
def sqr_list(num):
    data = ["{0}     {0}的平方是{1}".format(i, i ** 2) for i in range(1, num + 1)]

    return {'data': data}
