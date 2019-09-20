from django.shortcuts import render, redirect, HttpResponse

from django.views import View

from django.conf import global_settings
from django.contrib.sessions.backends import db

class Login(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username == 'alex' and pwd == '123':
            url = request.GET.get('return_url')
            if url:
                ret = redirect(url)
            else:
                ret = redirect('/index/')
            # ret['Set-Cookie'] = 'is_login=100; Path=/'
            # ret.set_cookie('is_login', '1')  # Set-Cookie: is_login=1; Path=/
            # ret.set_signed_cookie('is_login', '1', 's21',max_age=10000,)  # Set-Cookie: is_login=1; Path=/
            # 设置设session
            request.session['is_login'] = 1
            # request.session.set_expiry(0)
            return ret
        return render(request, 'login.html', {'error': '用户名或密码错误'})


def login_required(func):
    def inner(request, *args, **kwargs):
        # is_login = request.COOKIES.get('is_login')
        # is_login = request.get_signed_cookie('is_login', salt='s21', default='')
        is_login = request.session.get('is_login')
        print(is_login)
        url = request.path_info
        if is_login != 1:
            return redirect('/login/?return_url={}'.format(url))
        # 已经登录
        ret = func(request, *args, **kwargs)

        return ret

    return inner


@login_required
def index(request):
    # 获取到cookie
    print(request.session.session_key)
    request.session.clear_expired()

    return HttpResponse('首页')


@login_required
def home(request):
    return HttpResponse('home')


def logout(request):
    ret = redirect('/login/')
    # ret.delete_cookie('is_login')
    # request.session.delete()    # 删除session数据  不删除cookie
    request.session.flush()      # 删除session数据  删除cookie
    return ret
