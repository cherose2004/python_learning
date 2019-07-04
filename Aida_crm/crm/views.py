from django.shortcuts import render, redirect, reverse
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


users = [{'name': 'alex-{}'.format(i), 'pwd': 'alexdsb'} for i in range(1, 453)]


def user_list(request):
    try:
        page = int(request.GET.get('page', 1))
        if page <= 0:
            page = 1
    except Exception:
        page = 1

    # 总的数据量
    all_count = len(users)
    # 每页显示的数据量  10
    per_num = 10
    # 总的页码数
    total_num, more = divmod(all_count, per_num)
    if more:
        total_num += 1
    # 最大显示的页码数
    max_show = 11
    half_show = max_show // 2

    if total_num <= max_show:
        page_start = 1
        page_end = total_num
    else:
        if page - half_show<=0:
            # 页码的起始值
            page_start = 1
            # 页码的终止值
            page_end = max_show
        elif page + half_show > total_num:
            page_end = total_num
            page_start = total_num - max_show + 1

        else:
            # 页码的起始值
            page_start = page - half_show
            # 页码的终止值
            page_end = page + half_show
    #   1  0  10
    #   2  10  20
    start = (page - 1) * per_num
    end = page * per_num

    li_list = []

    if page == 1:
        li_list.append(
            '<li class="disabled"><a aria-label="Previous"> <span aria-hidden="true">&laquo;</span></a></li>')
    else:
        li_list.append('<li><a href="?page={}" aria-label="Previous"> <span aria-hidden="true">&laquo;</span></a></li>'.format(page-1))

    for i in range(page_start,page_end+1):
        if i == page:
            li_list.append('<li class="active"><a href="?page={}">{}</a></li>'.format(i, i))
        else:
            li_list.append('<li><a href="?page={}">{}</a></li>'.format(i,i))

    if page == total_num:
        li_list.append(
            '<li class="disabled"><a aria-label="Next"> <span aria-hidden="true">&raquo;</span></a></li>')
    else:
        li_list.append('<li><a href="?page={}" aria-label="Next"> <span aria-hidden="true">&raquo;</span></a></li>'.format(page+1))



    page_html = ''.join(li_list)

    return render(request, 'user_list.html', {'users': users[start:end],'page_html':page_html })
