from django.contrib import admin
from testapp.models import Cart
# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display = ['itemname','qty','price']

admin.site.register(Cart,CartAdmin)
