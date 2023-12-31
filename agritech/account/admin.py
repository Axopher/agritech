from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile

class CustomUserAdmin(UserAdmin):
    list_display = ('phone_number', 'user_name', 'role', 'is_active','is_verified')
    ordering = ('-date_joined',)
    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('phone_number', 'user_name','role', 'is_active')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser','is_verified')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )

admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)
