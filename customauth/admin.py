from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CustomUser, Order, Request


admin.site.site_header = 'AUTO SHOP'
admin.site.site_title = 'AUTO SHOP'
admin.site.index_title = 'AUTO SHOP'


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = 'username', 'last_name', 'first_name'
    list_filter = ('groups',)
    search_fields = 'username', 'last_name', 'first_name'


@admin.register(Request)
class RequestAdmin(ModelAdmin):
    list_display = 'subject', 'status'
    search_fields = 'name', 'subject', 'email'
    readonly_fields = 'name', 'subject', 'email', 'message'
    list_filter = ('status',)

    def has_add_permission(self, request):
        return False


@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_filter = 'auto', 'complete_set', 'manager', 'status'
    list_display = 'auto', 'complete_set', 'manager', 'first_name', 'last_name', 'status'
    search_fields = 'first_name', 'last_name', 'email', 'phone'
