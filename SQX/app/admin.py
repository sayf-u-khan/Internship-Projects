from django.contrib import admin

# Register your models here.

from .models import CustomUser
from django.contrib import admin
from .models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name')
    ordering = ('email',)
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('email', 'first_name', 'last_name', 'phone_number', 'profile_picture')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)

# Set a custom login template for the admin interface, and overridden the has_permission method to only allow superusers to access the admin interface.

admin.site.login_template = 'admin/login.html'

admin.site.has_permission = lambda request: request.user.is_superuser
