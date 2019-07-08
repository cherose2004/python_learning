from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
import hashlib
from crm.forms import RegForm, CustomerForm


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


def index(request):
    return render(request, 'index.html')


def customer_list(request):
    if request.path_info == reverse('customer_list'):
        all_customer = models.Customer.objects.filter(consultant__isnull=True)
    else:
        all_customer = models.Customer.objects.filter(consultant=request.user_obj)

    return render(request, 'customer_list.html', {'all_customer': all_customer})


from django.views import View


class CustomerList(View):

    def get(self, request, *args, **kwargs):
        if request.path_info == reverse('customer_list'):
            all_customer = models.Customer.objects.filter(consultant__isnull=True)
        else:
            all_customer = models.Customer.objects.filter(consultant=request.user_obj)

        return render(request, 'customer_list.html', {'all_customer': all_customer})

    def post(self, request, *args, **kwargs):
        action = request.POST.get('action')
        if not hasattr(self, action):
            return HttpResponse('非法操作')
        getattr(self, action)()
        return self.get(request, *args, **kwargs)

    def multi_apply(self):
        # 公户转私户
        pk = self.request.POST.getlist('pk')
        # 方法一
        models.Customer.objects.filter(pk__in=pk).update(consultant=self.request.user_obj)
        # 方法二
        # self.request.user_obj.customers.add(*models.Customer.objects.filter(pk__in=pk))

    def multi_pub(self):
        # 私户转公户
        pk = self.request.POST.getlist('pk')
        # 方法一
        models.Customer.objects.filter(pk__in=pk).update(consultant=None)
        # 方法二
        # self.request.user_obj.customers.remove(*models.Customer.objects.filter(pk__in=pk))


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

    return render(request, 'add_customer.html', {'form_obj': form_obj})


def edit_customer(request, pk):
    obj = models.Customer.objects.filter(pk=pk).first()
    # form_obj 包含原始的数据
    form_obj = CustomerForm(instance=obj)  # 实例  对象

    if request.method == 'POST':
        form_obj = CustomerForm(data=request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('customer_list'))
    return render(request, 'edit_customer.html', {'form_obj': form_obj})


def customer_change(request, pk=None):
    obj = models.Customer.objects.filter(pk=pk).first()

    form_obj = CustomerForm(instance=obj)
    if request.method == 'POST':
        form_obj = CustomerForm(data=request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('customer_list'))
    title = '编辑客户' if pk else '新增客户'
    return render(request, 'customer_form.html', {'form_obj': form_obj, 'title': title})


users = [{'name': 'alex-{}'.format(i), 'pwd': 'alexdsb'} for i in range(1, 453)]

from utils.pagination import Pagination


def user_list(request):
    page = Pagination(request.GET.get('page', 1), len(users), 20, 15)
    return render(request, 'user_list.html', {'users': users[page.start:page.end], 'page_html': page.page_html})
