from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['registration_number', 'full_name', 'email', 'course', 'semester', 'registration_date']
    list_filter = ['course', 'semester', 'gender', 'is_active']
    search_fields = ['full_name', 'registration_number', 'email']
    readonly_fields = ['registration_number', 'registration_date']
    fieldsets = (
        ('Personal Information', {
            'fields': ('registration_number', 'full_name', 'date_of_birth', 'gender', 'student_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone_number', 'address')
        }),
        ('Academic Information', {
            'fields': ('course', 'semester')
        }),
        ('Parent Information', {
            'fields': ('parent_name', 'parent_contact')
        }),
        ('Status', {
            'fields': ('is_active', 'registration_date')
        }),
    )