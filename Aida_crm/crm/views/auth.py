from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
import hashlib
from crm.forms import RegForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))

        obj = models.UserProfile.objects.filter(username=username, password=md5.hexdigest(), is_active=True).first()
        if obj:
            # 登录成功
            request.session['is_login'] = True
            request.session['user_id'] = obj.pk
            return redirect(reverse('index'))
            # return redirect('index')
        else:
            return render(request, 'login.html', {'error': '用户名或密码错误'})
    return render(request, 'login.html')


def reg(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        # 对提交的数据进行校验
        if form_obj.is_valid():
            # 校验成功  把数据插入数据中
            # form_obj.cleaned_data.pop('re_password')
            # models.UserProfile.objects.create(**form_obj.cleaned_data)
            obj = form_obj.save()
            return redirect(reverse('login'))
        print(form_obj.errors)
    return render(request, 'reg.html', {'form_obj': form_obj})
