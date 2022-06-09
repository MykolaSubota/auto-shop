from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser, Order


admin.site.site_header = 'AUTO SHOP'
admin.site.site_title = 'AUTO SHOP'
admin.site.index_title = 'AUTO SHOP'

admin.site.register(Order)


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = 'username', 'last_name', 'first_name'
    list_filter = ('groups',)
    search_fields = 'username', 'last_name', 'first_name'
