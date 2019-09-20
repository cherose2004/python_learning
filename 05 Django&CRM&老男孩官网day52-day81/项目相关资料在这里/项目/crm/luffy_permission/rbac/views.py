from django.shortcuts import render, HttpResponse, redirect, reverse
from rbac.forms import *
from rbac import models
from django.db.models import Q
from django.forms import modelformset_factory
from django.forms import formset_factory
from rbac.server.routes import get_all_url_dict


def role_list(request):
    """
    角色列表
    :param request:
    :return:
    """
    all_roles = models.Role.objects.all()
    return render(request, 'rbac/role_list.html', {"all_roles": all_roles})


def role(request, edit_id=None):
    """
    角色添加和编辑
    :param request:
    :param edit_id:
    :return:
    """
    obj = models.Role.objects.filter(id=edit_id).first()
    form_obj = RoleForm(instance=obj)
    if request.method == 'POST':
        form_obj = RoleForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:role_list'))

    return render(request, 'rbac/form.html', {'form_obj': form_obj})


def del_role(request, del_id):
    """
    删除角色
    :param request:
    :param del_id:
    :return:
    """
    models.Role.objects.filter(id=del_id).delete()
    return redirect(reverse('rbac:role_list'))


def menu_list(request):
    """
    权限信息展示（菜单和权限）
    :param request:
    :return:
    """
    all_menu = models.Menu.objects.all()

    mid = request.GET.get('mid')

    if mid:
        permission_query = models.Permission.objects.filter(Q(menu_id=mid) | Q(parent__menu_id=mid))
    else:
        permission_query = models.Permission.objects.all()
    permission_all = permission_query.values('id', 'title', 'url', 'name', 'parent_id', 'menu_id', 'menu__title')

    permission_dict = {}

    for item in permission_all:
        if item.get('menu_id'):
            item['children'] = []
            permission_dict[item['id']] = item

    for item in permission_all:
        pid = item.get('parent_id')
        if pid:
            permission_dict[pid]['children'].append(item)

    return render(request, 'rbac/menu_list.html',
                  {"all_menu": all_menu, 'permission_dict': permission_dict, 'mid': mid})


def menu(request, edit_id=None):
    """
    菜单添加和编辑
    :param request:
    :param edit_id:
    :return:
    """
    obj = models.Menu.objects.filter(id=edit_id).first()
    form_obj = MenuForm(instance=obj)
    if request.method == 'POST':
        form_obj = MenuForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:menu_list'))

    return render(request, 'rbac/menu_form.html', {'form_obj': form_obj})


def menu_del(request, del_id):
    """
    删除菜单
    :param request:
    :param del_id:
    :return:
    """
    models.Menu.objects.filter(id=del_id).delete()
    return redirect(reverse('rbac:menu_list'))


def permission(request, edit_id=None):
    """
    权限添加和编辑
    :param request:
    :param edit_id:
    :return:
    """
    obj = models.Permission.objects.filter(id=edit_id).first()
    form_obj = PermissionForm(instance=obj)
    if request.method == 'POST':
        form_obj = PermissionForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            return redirect(reverse('rbac:menu_list'))

    return render(request, 'rbac/form.html', {'form_obj': form_obj})


def permission_del(request, del_id):
    """
    删除权限
    :param request:
    :param del_id:
    :return:
    """
    models.Permission.objects.filter(id=del_id).delete()
    return redirect(reverse('rbac:menu_list'))


def multi_permissions(request):
    """
    批量操作权限
    :param request:
    :return:
    """
    post_type = request.GET.get('type')

    FormSet = modelformset_factory(models.Permission, MultiPermissionForm, extra=0)
    AddFormSet = formset_factory(MultiPermissionForm, extra=0)

    permissions = models.Permission.objects.all()
    router_dict = get_all_url_dict(ignore_namespace_list=['admin', ])

    permissions_name_set = set([i.name for i in permissions])

    router_name_set = set(router_dict.keys())

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

    del_name_set = permissions_name_set - router_name_set
    del_formset = FormSet(queryset=models.Permission.objects.filter(name__in=del_name_set))

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


def distribute_permissions(request):
    """
    分配权限
    :param request:
    :return:
    """
    uid = request.GET.get('uid')
    rid = request.GET.get('rid')

    if request.method == 'POST' and request.POST.get('postType') == 'role':
        user = models.User.objects.filter(id=uid).first()
        if not user:
            return HttpResponse('用户不存在')
        user.roles.set(request.POST.getlist('roles'))

    if request.method == 'POST' and request.POST.get('postType') == 'permission' and rid:
        role = models.Role.objects.filter(id=rid).first()
        if not role:
            return HttpResponse('角色不存在')
        role.permissions.set(request.POST.getlist('permissions'))

    user_list = models.User.objects.all()

    user_has_roles = models.User.objects.filter(id=uid).values('id', 'roles')

    user_has_roles_dict = {item['roles']: None for item in user_has_roles}

    role_list = models.Role.objects.all()

    if rid:
        role_has_permissions = models.Role.objects.filter(id=rid, permissions__id__isnull=False).values('id',
                                                                                                        'permissions')
    elif uid and not rid:
        user = models.User.objects.filter(id=uid).first()
        if not user:
            return HttpResponse('用户不存在')
        role_has_permissions = user.roles.filter(permissions__id__isnull=False).values('id', 'permissions')
    else:
        role_has_permissions = []

    role_has_permissions_dict = {item['permissions']: None for item in role_has_permissions}

    all_menu_list = []

    queryset = models.Menu.objects.values('id', 'title')
    menu_dict = {}

    for item in queryset:
        item['children'] = []
        menu_dict[item['id']] = item
        all_menu_list.append(item)

    other = {'id': None, 'title': '其他', 'children': []}
    all_menu_list.append(other)
    menu_dict[None] = other

    root_permission = models.Permission.objects.filter(menu__isnull=False).values('id', 'title', 'menu_id')
    root_permission_dict = {}

    for per in root_permission:
        per['children'] = []
        nid = per['id']
        menu_id = per['menu_id']
        root_permission_dict[nid] = per
        menu_dict[menu_id]['children'].append(per)

    node_permission = models.Permission.objects.filter(menu__isnull=True).values('id', 'title', 'parent_id')

    for per in node_permission:
        pid = per['parent_id']
        if not pid:
            menu_dict[None]['children'].append(per)
            continue
        root_permission_dict[pid]['children'].append(per)

    return render(
        request,
        'rbac/distribute_permissions.html',
        {
            'user_list': user_list,
            'role_list': role_list,
            'user_has_roles_dict': user_has_roles_dict,
            'role_has_permissions_dict': role_has_permissions_dict,
            'all_menu_list': all_menu_list,
            'uid': uid,
            'rid': rid
        }
    )
