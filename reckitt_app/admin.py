# reckitt_app/admin.py

from django.contrib import admin
from .models import LineUser

@admin.register(LineUser)
class LineUserAdmin(admin.ModelAdmin):
    list_display = ('display_name', 'line_id', 'first_name', 'last_name', 'employee_id', 'department', 'created_at')
    search_fields = ('display_name', 'line_id', 'first_name', 'last_name', 'employee_id')
    list_filter = ('department', 'created_at')
    ordering = ('-created_at',)