from django.shortcuts import render, HttpResponse

from django import forms
from app01 import models

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator


def checkname(value):
    # 通过校验规则 不做任何操作
    # 不通过校验规则   抛出异常
    if 'alex' in value:
        raise ValidationError('不符合社会主义核心价值观')


class RegForm(forms.Form):
    username = forms.CharField(
        label='用户名',
        min_length=6,
        initial='张三',
        required=True,
        validators=[],
        error_messages={
            'required': '用户名是必填项',
            'min_length': '用户名长度不能小于6位'
        }
    )
    pwd = forms.CharField(label='密码', widget=forms.PasswordInput)
    re_pwd = forms.CharField(label='确认密码', widget=forms.PasswordInput)
    gender = forms.ChoiceField(
        choices=((1, '男'), (2, '女')),
        widget=forms.RadioSelect
    )
    # hobby = forms.MultipleChoiceField(
    #     # choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
    #     choices=models.Hobby.objects.values_list('id', 'name'),
    # )

    hobby = forms.ModelMultipleChoiceField(
        # choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        queryset=models.Hobby.objects.all(),
    )

    phone = forms.CharField(
        validators=[RegexValidator(r'^1[3-9]\d{9}$', '手机号格式不正确')]
    )

    def clean_username(self):
        # 局部钩子
        # 通过校验规则  必须返回当前字段的值
        # 不通过校验规则   抛出异常
        v = self.cleaned_data.get('username')
        if 'alex' in v:
            raise ValidationError('不符合社会主义核心价值观')
        else:
            return v

    def clean(self):
        # 全局钩子
        # 通过校验规则  必须返回当前所有字段的值
        # 不通过校验规则   抛出异常   '__all__'
        pwd = self.cleaned_data.get('pwd')
        re_pwd = self.cleaned_data.get('re_pwd')

        if pwd == re_pwd:
            return self.cleaned_data
        else:
            self.add_error('re_pwd','两次密码不一致!!!!!')
            raise ValidationError('两次密码不一致')

    # def __init__(self, *args, **kwargs):
    #     super(RegForm, self).__init__(*args, **kwargs)
    #     self.fields['hobby'].choices = models.Hobby.objects.values_list('id', 'name')


def reg(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if len(username) < 6:
            return render(request, 'reg.html', {'error': '用户名长度不能小于6位'})

        return HttpResponse('注册成功')

    return render(request, 'reg.html')


def reg2(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():  # 对数据进行校验
            # 插入数据
            print(form_obj.cleaned_data)  # 通过校验的数据
            return HttpResponse('注册成功')

    return render(request, 'reg2.html', {'form_obj': form_obj})
