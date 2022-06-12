from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Auto, Part, CompleteSet


@admin.register(Auto)
class AutoAdmin(ModelAdmin):
    search_fields = ('name',)


@admin.register(CompleteSet)
class CompleteSetAdmin(ModelAdmin):
    list_filter = ('parts',)


@admin.register(Part)
class PartAdmin(ModelAdmin):
    list_filter = ('type',)
    list_display = 'name', 'type'
    search_fields = ('name',)
