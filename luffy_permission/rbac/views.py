from django.shortcuts import render, redirect, reverse
from rbac import models
from rbac.forms import RoleForm


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
