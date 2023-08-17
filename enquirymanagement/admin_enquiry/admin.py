from django.contrib import admin

from .models import AdminDatabase

class enquiryadmin(admin.ModelAdmin):
    list_display=('id','Firstname','Lastname','Email','Contact','Password')
admin.site.register(AdminDatabase,enquiryadmin)