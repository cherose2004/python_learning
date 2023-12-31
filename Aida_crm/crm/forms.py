from crm import models
from django import forms
from django.core.exceptions import ValidationError
import hashlib
from multiselectfield.forms.fields import MultiSelectFormField


class BSModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            if isinstance(filed, (MultiSelectFormField, forms.BooleanField)):
                continue
            filed.widget.attrs['class'] = 'form-control'


class RegForm(forms.ModelForm):
    password = forms.CharField(min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': '您的密码', 'autocomplete': 'off'}))
    re_password = forms.CharField(min_length=6,
                                  widget=forms.PasswordInput(attrs={'placeholder': '您的确认密码', 'autocomplete': 'off'}))

    class Meta:
        model = models.UserProfile
        fields = '__all__'  # ['username']
        exclude = ['is_active']
        labels = {
            'username': '用户名'
        }
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': '您的用户名', 'autocomplete': 'off', }),
            # 'password':forms.PasswordInput(attrs={'placeholder':'您的密码','autocomplete':'off'}),
            'mobile': forms.TextInput(attrs={'placeholder': '您的手机号', 'autocomplete': 'off'}),
            'name': forms.TextInput(attrs={'placeholder': '您的真实姓名', 'autocomplete': 'off'})
        }
        error_messages = {
            'username': {
                'required': '必填',
                'invalid': '邮箱格式不正确'
            }
        }

    def clean(self):
        self._validate_unique = True
        password = self.cleaned_data.get('password', '')
        re_password = self.cleaned_data.get('re_password', '')
        if password == re_password:
            # 对密码进行加密
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md5.hexdigest()
            return self.cleaned_data
        else:
            self.add_error('re_password', '两次密码不一致')
            raise ValidationError('两次密码不一致!!')


class CustomerForm(BSModelForm):
    class Meta:
        model = models.Customer
        fields = "__all__"
        exclude = []
        labels = {

        }

        # widgets = {
        # 'qq': forms.TextInput(attrs={'class': 'form-control'}),
        # }


class ConsultRecordForm(BSModelForm):
    class Meta:
        model = models.ConsultRecord
        fields = '__all__'

    def __init__(self, request, customer_id, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # print(list(self.fields['customer'].choices))
        # self.fields['customer'].choices = [('', '---------'), (1, '121312321321 - mjj')]
        # self.fields['customer'].choices = request.user_obj.customers.all().values_list('pk','name')
        print(customer_id)
        # 限制咨询客户为当前销售的私户
        if customer_id and customer_id != '0':
            self.fields['customer'].choices = [(i.pk, str(i)) for i in models.Customer.objects.filter(pk=customer_id)]
        else:
            self.fields['customer'].choices = [('', '---------'), ] + [(i.pk, str(i)) for i in
                                                                       request.user_obj.customers.all()]

        # 限制跟进人为当前销售
        self.fields['consultant'].choices = [(request.user_obj.pk, request.user_obj)]


class EnrollmentForm(BSModelForm):
    class Meta:
        model = models.Enrollment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 限制客户为当前销售的私户

        # self.instance  # models.Enrollment(customer_id=customer_id)
        self.fields['customer'].choices = [(self.instance.customer.pk, self.instance.customer)]

        self.fields['enrolment_class'].choices = [(i.pk, str(i)) for i in self.instance.customer.class_list.all()]


class ClassListForm(BSModelForm):
    class Meta:
        model = models.ClassList
        fields = "__all__"


class CourseRecordForm(BSModelForm):
    class Meta:
        model = models.CourseRecord
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 限制班级为当前的班级
        self.fields['re_class'].choices = [(self.instance.re_class_id, self.instance.re_class)]

        # 限制记录者为当前的用户
        self.fields['recorder'].choices = [(self.instance.recorder_id, self.instance.recorder)]

        #  限制讲师为当前的班级的讲师
        self.fields['teacher'].choices = [(i.pk, str(i)) for i in self.instance.re_class.teachers.all()]


class StudyRecordForm(BSModelForm):
    class Meta:
        model = models.StudyRecord
        fields = "__all__"
