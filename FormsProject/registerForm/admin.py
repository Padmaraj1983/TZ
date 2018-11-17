from django.contrib import admin
from registerForm.models import Register
# Register your models here.
class RegisterAdmin(admin.ModelAdmin):
    list_display = ['uname','password','rpassword']


admin.site.register(Register,RegisterAdmin)