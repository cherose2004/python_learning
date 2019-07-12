from django.shortcuts import render, reverse, redirect

from rbac import models
from django.conf import settings


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        obj = models.User.objects.filter(username=username, password=password).first()
        if not obj:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
        # 登录成功
        # 获取权限
        permissions = obj.roles.filter(permissions__url__isnull=False).values(
            'permissions__url',
            'permissions__title',
            'permissions__icon',
            'permissions__is_menu',
        ).distinct()
        # 权限信息的列表
        permission_list = []
        # 菜单信息的列表
        menu_list = []  # [{  url   title  icon   }]

        for i in permissions:  # {  'permissions__url', }
            permission_list.append({'url': i['permissions__url']})

            if i['permissions__is_menu']:
                menu_list.append({
                    'url': i['permissions__url'],
                    'title': i['permissions__title'],
                    'icon': i['permissions__icon'],
                })

        # 保存到session中
        request.session[settings.PERMISSION_SESSION_KEY] = permission_list  # json序列化
        request.session[settings.MENU_SESSION_KEY] = menu_list  # json序列化
        request.session['is_login'] = True
        return redirect(reverse('index'))

    return render(request, 'login.html')
