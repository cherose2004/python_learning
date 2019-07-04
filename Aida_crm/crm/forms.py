from crm import models
from django import forms
from django.core.exceptions import ValidationError
import hashlib


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
