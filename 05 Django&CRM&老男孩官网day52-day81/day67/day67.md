## 内容回顾

```python
class RegForm(forms.Form):
    username = forms.CharField(
        min_length=6,
        max_length=32,
        label='用户名',
        initial='初始值',
        error_messages={
            'required':'必填',
            'min_length':'最小长度',
            'invalid':''
        },
        validators=[],
        widget=forms.TextInput(attrs={''})
    )
    gender = forms.ChoiceField(choices=[(1,'男'),(2,'女')])


    def clean_username(self):
        pass
        # 校验成功 返回该字段的值
        # 校验不成功  抛出异常

    def clean(self):
        pass
        # 校验成功 返回所有的值
        # 校验不成功  抛出异常  __all__
        # self.add_error(filed,error)
        
        
        
class RegForm(forms.ModelForm):
    password = forms.CharField(min_length=6,
                               widget=forms.PasswordInput(attrs={'placeholder': '您的密码', 'autocomplete': 'off'}))
    re_password = forms.CharField(min_length=6,
                                  widget=forms.PasswordInput(attrs={'placeholder': '您的确认密码', 'autocomplete': 'off'}))

    class Meta:
        model = models.UserProfile
        fields = '__all__'  # ['username']
        exclude = ['is_active']
        labels={
            'username':'用户名'
        }
        widgets = {
            'username': forms.EmailInput(attrs={'placeholder': '您的用户名', 'autocomplete': 'off',}),
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
        password = self.cleaned_data.get('password','')
        re_password = self.cleaned_data.get('re_password','')
        if password == re_password:
            # 对密码进行加密
            md5 = hashlib.md5()
            md5.update(password.encode('utf-8'))
            self.cleaned_data['password'] = md5.hexdigest()
            return self.cleaned_data
        else:
            self.add_error('re_password', '两次密码不一致')
            raise ValidationError('两次密码不一致!!')

```

## 今日内容

### 1.展示客户信息

1.普通的字段

对象.字段名

2.有choice参数

对象.字段名   —— 》 数据库的数据

`对象.get_字段名_display()`      —— 》 数据库的数据对应的中文提示

3.外键

对象.外键  ——》  外键对象   定义`__str__`

对象.外键.字段

4.自定义方法：

多对多：

```python
def show_class(self):
    return ' '.join([str(i) for i in self.class_list.all()])
```

自定义的需求：

```python
def show_status(self):
    color_dict = {
        'signed': "green",
        'unregistered': 'red',
        'studying': 'blue',
        'paid_in_full': 'gold'
    }
    return mark_safe(
        '<span style="color: white;background: {};padding: 5px" >{}</span>'.format(color_dict.get(self.status),self.get_status_display()))
```

### 2.分页

见代码

### 3.git版本回退

git reset --hard 版本号

git log 

git reflog

### 4. 克隆 推送 拉取

git clone https://gitee.com/old_boy_python_stack_21/teaching_plan.git  克隆远程仓库

git push origin master 推送本地代码到远程仓库

git pull origin master  拉取远程仓库代码到本地仓库



