from django.contrib import admin
from filterapp.models import FilterDemo
# Register your models here.
class FilterModelAdmin(admin.ModelAdmin):
    list_display=['name','subject','dept','date']

admin.site.register(FilterDemo,FilterModelAdmin)