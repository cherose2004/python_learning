from django import forms
from rbac import models


class BSModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BSModelForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'


class RoleForm(BSModelForm):
    class Meta:
        model = models.Role
        fields = ['name']
