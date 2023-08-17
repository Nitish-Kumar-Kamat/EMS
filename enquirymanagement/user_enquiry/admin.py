from django.contrib import admin

from .models import UserDatabase,EnquiryDatabase

class useradmin(admin.ModelAdmin):
    list_display=('id','Firstname','Lastname','Email','Contact','Password')
admin.site.register(UserDatabase,useradmin)

class enquiryadmin(admin.ModelAdmin):
    list_display=('id','Name','Email','Contact','Address','Query')
admin.site.register(EnquiryDatabase,enquiryadmin)