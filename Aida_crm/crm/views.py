from django.shortcuts import render, redirect, reverse, HttpResponse
from crm import models
import hashlib
from crm.forms import RegForm, CustomerForm, ConsultRecordForm


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
from django.db.models import Q
from utils.pagination import Pagination

from django.http.request import QueryDict


class CustomerList(View):

    def get(self, request, *args, **kwargs):

        # print(request.GET,type(request.GET))
        # print(request.GET.urlencode())
        # request.GET._mutable = True  # 可编辑
        # request.GET['page'] = 1
        # print(request.GET.urlencode())

        q = self.search(['qq', 'name', 'phone', 'consultant__name'])

        if request.path_info == reverse('customer_list'):
            all_customer = models.Customer.objects.filter(q, consultant__isnull=True)
        else:
            all_customer = models.Customer.objects.filter(q, consultant=request.user_obj)

        page = Pagination(request.GET.get('page', 1), all_customer.count(), request.GET.copy(), 2)

        return render(request, 'customer_list.html',
                      {'all_customer': all_customer[page.start:page.end], 'page_html': page.page_html})

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

    def search(self, field_list):
        # 构建Q对象
        # Q(Q(qq__contains=query) | Q(name__contains=query) | Q(phone__contains=query))

        query = self.request.GET.get('query', '')
        q = Q()
        q.connector = 'OR'
        for field in field_list:
            q.children.append(Q(('{}__contains'.format(field), query)))
        return q


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
            next = request.GET.get('next')
            print(next)
            if next:
                return redirect(next)
            return redirect(reverse('customer_list'))
    title = '编辑客户' if pk else '新增客户'
    return render(request, 'form.html', {'form_obj': form_obj, 'title': title})


users = [{'name': 'alex-{}'.format(i), 'pwd': 'alexdsb'} for i in range(1, 453)]

from utils.pagination import Pagination


def user_list(request):
    page = Pagination(request.GET.get('page', 1), len(users), 20, 15)
    return render(request, 'user_list.html', {'users': users[page.start:page.end], 'page_html': page.page_html})


class ConsultList(View):

    def get(self, request, customer_id=None, *args, **kwargs):
        if not customer_id:
            # 展示当前销售的所有的跟进记录
            all_consult = models.ConsultRecord.objects.filter(consultant=request.user_obj, delete_status=False)
        else:
            # 某一个客户的所有的跟进记录
            all_consult = models.ConsultRecord.objects.filter(customer_id=customer_id, delete_status=False)
        return render(request, 'consult_list.html', {'all_consult': all_consult.order_by('-date')})


def consult_change(request, pk=None):
    obj = models.ConsultRecord.objects.filter(pk=pk).first()
    form_obj = ConsultRecordForm(request,instance=obj)
    if request.method == 'POST':
        form_obj = ConsultRecordForm(request,request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('consult_list'))

    title = '编辑跟进' if pk else '新增跟进'
    return render(request, 'form.html', {'form_obj': form_obj, 'title': title})
