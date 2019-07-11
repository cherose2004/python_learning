from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.shortcuts import redirect, HttpResponse
from django.conf import settings
import re


class AuthMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        # 获取当前访问的URL
        path = request.path_info
        # 白名单
        for url in settings.WHITE_LIST:
            if re.match(url, path):
                return
        # 登录状态的校验
        is_login = request.session.get('is_login')
        if not is_login:
            return redirect(reverse('login'))
        # 免认证的校验
        for url in settings.NO_PERMISSION_LIST:
            if re.match(url, path):
                return
        # 获取权限信息
        permissions = request.session.get('permissions')
        # 权限的校验
        for permission in permissions:
            if re.match(permission['permissions__url'], path):
                return
        return HttpResponse('没有访问权限,请联系管理员')
