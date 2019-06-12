from django.shortcuts import HttpResponse, render, redirect
from app01 import models


def index(request):
    # return HttpResponse('index')
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        # 获取form表单提交的书籍
        username = request.POST['username']
        password = request.POST['password']
        # 验证用户名和密码
        if models.User.objects.filter(username=username,password=password):
            # 验证成功跳转到index页面
            # return redirect('https://www.baidu.com/')
            return redirect('/index/')
        # 不成功 重新登录
    return render(request, 'login.html')



def orm_test(request):
    # ORM操作
    # 获取表中所有的数据
    ret = models.User.objects.all()  # QuerySet 对象列表
    # for i in ret:
    #     print(i.username,i.password)

    # obj = models.User.objects.get(username='alex')   # 获取不到或者获取到多个对象会报错
    # 获取满足条件的对象
    ret = models.User.objects.filter(username='alex1',password='dasb')  # QuerySet 对象列表
    print(ret,type(ret))

    return HttpResponse('ok')
