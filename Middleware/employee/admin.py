from django.contrib import admin
from employee.models import emp

# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display = ('name', 'emp_id', 'department')

admin.site.register(emp, EmpAdmin)
