"""s2123djngoday URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views import View
from django.shortcuts import render,HttpResponse
class LoginView(View):

    def get(self,request,*args,**kwargs):
        print('用户来访问了')
        return render(request,'login.html')
    def post(self,request,*args,**kwargs):
        print('用户提交数据来了')
        return HttpResponse('提交成功')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/',LoginView.as_view() ),
]
