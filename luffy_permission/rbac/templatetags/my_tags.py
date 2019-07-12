from django import template
from django.conf import settings
import re
register = template.Library()


@register.inclusion_tag('rbac/menu.html')
def menu(request):
    menu_dict = request.session.get(settings.MENU_SESSION_KEY)
    url = request.path_info

    return {'menu_list': menu_dict.values()}
