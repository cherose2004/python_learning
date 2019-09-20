from django.views import View
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.db.models import Q


class BaseView(View):

    def post(self, request, *args, **kwargs):

        action = request.POST.get('action')
        if not hasattr(self, action):
            return HttpResponse('非法操作')
        ret = getattr(self, action)()
        if ret:
            return ret
        return self.get(request, *args, **kwargs)

    def search(self, field_list):
        # 构建Q对象
        # Q(Q(qq__contains=query) | Q(name__contains=query) | Q(phone__contains=query))

        query = self.request.GET.get('query', '')
        q = Q()
        q.connector = 'OR'
        for field in field_list:
            q.children.append(Q(('{}__contains'.format(field), query)))
        return q
