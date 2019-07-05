from django.shortcuts import render, redirect, reverse
from crm import models
import hashlib
from crm.forms import RegForm,CustomerForm


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))

        obj = models.UserProfile.objects.filter(username=username, password=md5.hexdigest(), is_active=True).first()
        if obj:
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


def index(request):
    return render(request, 'index.html')


def customer_list(request):
    all_customer = models.Customer.objects.all()
    return render(request, 'customer_list.html', {'all_customer': all_customer})


def add_customer(request):
    # form_obj 没有数据
    form_obj = CustomerForm()
    if request.method == 'POST':
        # form_obj 包含提交的数据
        form_obj = CustomerForm(request.POST)
        if form_obj.is_valid():
            # 校验成功
            form_obj.save()
            return redirect(reverse('customer_list'))

    return render(request,'add_customer.html',{'form_obj':form_obj})



users = [{'name': 'alex-{}'.format(i), 'pwd': 'alexdsb'} for i in range(1, 453)]

from utils.pagination import Pagination


def user_list(request):
    page = Pagination(request.GET.get('page', 1), len(users), 20, 15)
    return render(request, 'user_list.html', {'users': users[page.start:page.end], 'page_html': page.page_html})
