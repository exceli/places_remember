from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'phone_number', 'first_name', 'last_name', 'is_staff', 'is_superuser']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone_number',)}),
    )



admin.site.register(CustomUser, CustomUserAdmin)