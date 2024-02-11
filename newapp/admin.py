from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group, User


class CustomUserAdmin(UserAdmin):
    list_display = (
        "username",
        "email",
        "first_name",
        "user_groups",
        "last_name",
        "is_staff",
        "date_joined",
        "last_login",
    )
    search_fields = ("username", "email", "first_name", "last_name")
    list_filter = ("is_staff", "is_superuser", "is_active")

    def user_groups(self, obj):
        return ", ".join([group.name for group in obj.groups.all()])


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
