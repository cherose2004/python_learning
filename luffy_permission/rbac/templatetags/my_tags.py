from django import template
from django.conf import settings
import re

register = template.Library()
from collections import OrderedDict


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    url = request.path_info
    od = OrderedDict()
    keys_list = sorted(menu_dict, key=lambda x: menu_dict[x]['weight'], reverse=True)

    for key in keys_list:
        od[key] = menu_dict[key]

    for i in menu_dict.values():
        i['class'] = 'hide'
        for m in i['children']:
            if re.match(r'{}$'.format(m['url']), url):
                m['class'] = 'active'
                i['class'] = ''

    print(od.values())
    return {'menu_list': od.values()}
