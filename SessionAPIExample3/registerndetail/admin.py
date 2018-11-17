from django.contrib import admin
from registerndetail.models import EmployeeModel
# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name','age','desig']

admin.site.register(EmployeeModel)
