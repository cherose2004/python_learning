from django.shortcuts import render, redirect, reverse
from rbac import models
from rbac.forms import RoleForm, MenuForm, PermissionForm, MultiPermissionForm
from rbac.service.routes import get_all_url_dict


def role_list(request):
    all_roles = models.Role.objects.all()
    return render(request, 'rbac/role_list.html', {'all_roles': all_roles})


def role_change(request, pk=None):
    obj = models.Role.objects.filter(pk=pk).first()
    form_obj = RoleForm(instance=obj)
    if request.method == 'POST':
        form_obj = RoleForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('role_list'))
    return render(request, 'form.html', {'form_obj': form_obj})


from django.db.models import Q


def menu_list(request):
    mid = request.GET.get('mid')

    all_menus = models.Menu.objects.all()
    if not mid:
        all_permissions = models.Permission.objects.all()
    else:
        all_permissions = models.Permission.objects.filter(Q(menu_id=mid) | Q(parent__menu_id=mid))

    """
    { id : {
                children： [ {}  {} ]
         } 
    }

    """
    permission_dict = {}

    for i in all_permissions.values('id', 'title', 'url', 'name', 'menu_id', 'menu__title', 'parent_id'):
        menu_id = i.get('menu_id')
        if menu_id:
            permission_dict[i['id']] = i
            i['children'] = []

    for i in all_permissions.values('id', 'title', 'url', 'name', 'menu_id', 'menu__title', 'parent_id'):
        pid = i.get('parent_id')
        if pid:
            permission_dict[pid]['children'].append(i)

    print(permission_dict)

    return render(request, 'rbac/menu_list.html', {
        'all_menus': all_menus,
        'all_permissions': permission_dict.values(),
        'mid': mid
    })


def menu_change(request, pk=None):
    obj = models.Menu.objects.filter(pk=pk).first()
    form_obj = MenuForm(instance=obj)
    if request.method == 'POST':
        form_obj = MenuForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('menu_list'))
    return render(request, 'form.html', {'form_obj': form_obj})


def permission_change(request, pk=None):
    obj = models.Permission.objects.filter(pk=pk).first()
    form_obj = PermissionForm(instance=obj)
    if request.method == 'POST':
        form_obj = PermissionForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('menu_list'))
    return render(request, 'form.html', {'form_obj': form_obj})


def delete(request, table, pk):
    table_class = getattr(models, table.capitalize())
    table_class.objects.filter(pk=pk).delete()
    if table == 'permission':
        return redirect(reverse('menu_list'))
    return redirect(reverse('{}_list'.format(table)))


# 批量操作权限
from django.forms import modelformset_factory, formset_factory


def multi_permissions(request):
    """
    批量操作权限
    :param request:
    :return:
    """
    post_type = request.GET.get('type')
    # 更新和删除
    FormSet = modelformset_factory(models.Permission, MultiPermissionForm, extra=0)
    # 新增
    AddFormSet = formset_factory(MultiPermissionForm, extra=0)

    # 数据库所有的权限
    permissions = models.Permission.objects.all()
    # 路由系统中所有的权限
    router_dict = get_all_url_dict(ignore_namespace_list=['admin', ])

    # 数据库权限的别名的集合
    permissions_name_set = set([i.name for i in permissions])
    # 路由系统中权限的别名的集合
    router_name_set = set(router_dict.keys())

    # 新增权限的别名的集合
    add_name_set = router_name_set - permissions_name_set
    add_formset = AddFormSet(initial=[row for name, row in router_dict.items() if name in add_name_set])

    if request.method == 'POST' and post_type == 'add':
        add_formset = AddFormSet(request.POST)
        if add_formset.is_valid():
            permission_obj_list = [models.Permission(**i) for i in add_formset.cleaned_data]
            query_list = models.Permission.objects.bulk_create(permission_obj_list)
            add_formset = AddFormSet()
            for i in query_list:
                permissions_name_set.add(i.name)

    # 删除的name的集合
    del_name_set = permissions_name_set - router_name_set
    del_formset = FormSet(queryset=models.Permission.objects.filter(name__in=del_name_set))
    # 更新的name的集合
    update_name_set = permissions_name_set & router_name_set
    update_formset = FormSet(queryset=models.Permission.objects.filter(name__in=update_name_set))

    if request.method == 'POST' and post_type == 'update':
        update_formset = FormSet(request.POST)
        if update_formset.is_valid():
            update_formset.save()
            update_formset = FormSet(queryset=models.Permission.objects.filter(name__in=update_name_set))

    return render(
        request,
        'rbac/multi_permissions.html',
        {
            'del_formset': del_formset,
            'update_formset': update_formset,
            'add_formset': add_formset,
        }
    )
