from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel, Profile


class CustomUserAdmin(UserAdmin):
    model = UserModel
    list_display = (
        "email",
        "first_name",
        "last_name",
        "mobile",
        "is_active",

    )
    list_filter = ("is_staff", "is_active", "date_joined")
    search_fields = ("email", "first_name", "last_name", "mobile")
    ordering = ("-date_joined",)

    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal Info", {"fields": ("first_name", "last_name", "mobile")}),
        ("Permissions", {"fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")}),
        ("Important Dates", {"fields": ("last_login", "date_joined")}),
    )

    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "mobile", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )

    readonly_fields = ('is_active', 'is_staff')

class ProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "gender", "address")
    list_filter = ("role", "gender")
    search_fields = ("user__email", "user__mobile", "address")


admin.site.register(UserModel, CustomUserAdmin)
admin.site.register(Profile, ProfileAdmin)
