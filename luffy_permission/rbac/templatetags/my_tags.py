from django import template
from django.conf import settings
import re
register = template.Library()


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_list = request.session.get(settings.MENU_SESSION_KEY)
    url = request.path_info
    for i in menu_list:
        if re.match(r'{}$'.format(i['url']),url):
            i['class'] = 'active'
            break

    return {'menu_list': menu_list,'url':url}
