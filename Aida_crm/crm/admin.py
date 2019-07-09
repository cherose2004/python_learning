from django.contrib import admin
from crm import models

admin.site.register(models.Customer)
admin.site.register(models.ClassList)
admin.site.register(models.Campus)
admin.site.register(models.ConsultRecord)
admin.site.register(models.Enrollment)