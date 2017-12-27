from django.contrib import admin
from .models import UserInfo

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','info')
    list_filter = ('age',)

admin.site.register(UserInfo,UserInfoAdmin)
# Register your models here.
