from django.contrib import admin
from tradezone.models import BeginnersGuide
# Register your models here.

class BeginnersGuideAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'body','text1','text2','text3','text4','text5','text6','text7','text8','publish', 'created', 'updated', 'status']
    list_filter = ['status', 'author', 'created', 'updated']
    search_fields = ['title', 'body']
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(BeginnersGuide,BeginnersGuideAdmin)