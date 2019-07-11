from django.shortcuts import render, reverse, redirect

from rbac import models


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
        permissions = obj.roles.filter(permissions__url__isnull=False).values('permissions__url').distinct()
        # 保存到session中
        request.session['permissions'] = list(permissions)
        request.session['is_login'] = True
        return redirect(reverse('index'))

    return render(request, 'login.html')
