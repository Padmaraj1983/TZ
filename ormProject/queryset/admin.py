from django.contrib import admin
from queryset.models import Employee
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','sal']

admin.site.register(Employee,EmployeeAdmin)

