from django.shortcuts import render, redirect, HttpResponse
from app01 import models


# 展示出版社
def publisher_list(request):
    # 从数据库中查询到出版社的信息
    all_publishers = models.Publisher.objects.all().order_by('pk')
    # 返回一个包含出版社信息的页面
    return render(request, 'publisher_list.html', {'all_publishers': all_publishers})


# 新增出版社
def add_publisher(request):
    # 对请求方式进行判断
    if request.method == 'POST':
        # 处理POST请求
        # 获取到出版社的名称
        publisher_name = request.POST.get('publisher_name')
        # 判断出版社名称是否有重复的
        if models.Publisher.objects.filter(name=publisher_name):
            return render(request, 'add_publisher.html', {'error': '出版社名称已存在'})
        # 判断输入的值是否为空
        if not publisher_name:
            return render(request, 'add_publisher.html', {'error': '不能输入为空'})
        # 使用ORM将数据插入到数据库中
        obj = models.Publisher.objects.create(name=publisher_name)
        # 跳转到展示出版社的页面
        return redirect('/publisher_list/')
    # 返回一个包含form表单的页面
    return render(request, 'add_publisher.html')


# 新增出版社
def add_publisher(request):
    error = ''
    # 对请求方式进行判断
    if request.method == 'POST':
        # 处理POST请求
        # 获取到出版社的名称
        publisher_name = request.POST.get('publisher_name')
        # 判断出版社名称是否有重复的
        if models.Publisher.objects.filter(name=publisher_name):
            error = '出版社名称已存在'
        # 判断输入的值是否为空
        if not publisher_name:
            error = '不能输入为空'
        if not error:
            # 使用ORM将数据插入到数据库中
            obj = models.Publisher.objects.create(name=publisher_name)
            # 跳转到展示出版社的页面
            return redirect('/publisher_list/')
    # 返回一个包含form表单的页面
    return render(request, 'add_publisher.html', {'error': error})


# 删除出版社
def del_publisher(request):
    # 获取要删除的数据
    pk = request.GET.get('id')
    obj_list = models.Publisher.objects.filter(pk=pk)
    if not obj_list:
        # 没有要删除的数据
        return HttpResponse('要删除的数据不存在')
    # 删除该数据
    # obj.delete()
    obj_list.delete()
    # 跳转到展示页面
    return redirect('/publisher_list/')


# 编辑出版社
def edit_publisher(request):
    error = ''
    # 查找要编辑的数据
    pk = request.GET.get('id')  # url上携带的参数  不是GET请求提交参数
    obj_list = models.Publisher.objects.filter(pk=pk)
    if not obj_list:
        return HttpResponse('要编辑的数据不存在')

    obj = obj_list[0]

    if request.method == 'POST':
        # 处理POST请求
        # 获取新提交的出版的名称
        publisher_name = request.POST.get('publisher_name')

        if models.Publisher.objects.filter(name=publisher_name):
            # 新修改的名称已存在
            error = '新修改的名称已存在'
        if obj.name == publisher_name:
            error = '名称未修改'
        if not publisher_name:
            error = '名称不能为空'

        if not error:
            # 修改数据
            obj.name = publisher_name
            obj.save()  # 保存数据到数据库中
            # 跳转到出版社的展示页面
            return redirect('/publisher_list/')

    # 返回一个包含原始数据的页面
    return render(request, 'edit_publisher.html', {'obj': obj,'error':error})
