from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(ManagementStaff)
class ManagementStaffAdmin(admin.ModelAdmin):
    list_field = [field.name for field in ManagementStaff._meta.get_fields() if not field.is_relation ]
    list_field.remove('password')
    list_display = ['name', 'email', 'is_active', 'is_staff']
    list_display_links = ['email']

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Doctor._meta.get_fields() if not field.is_relation]
    list_filter = ['specialization']
    list_display_links = ['name']

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Patient._meta.get_fields() if not field.is_relation]
    list_filter = ['gender']
    list_display_links = ['name']