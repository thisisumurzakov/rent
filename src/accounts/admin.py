from django.conf import settings
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from rest_framework_simplejwt.token_blacklist.admin import (
    OutstandingTokenAdmin,
)
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

from .models import User


class UserAdmin(BaseUserAdmin):
    list_display = (
        "guid",
        "phone_number",
        "first_name",
        "last_name",
        "is_staff",
    )

    list_filter = (
        "is_staff",
    )
    fieldsets = (
        (None, {"fields": ("phone_number", "password")}),
        (
            "Personal info",
            {
                "fields": (
                    "first_name",
                    "last_name"
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )

    add_fieldsets = (
        (
            None,
            {"fields": ("phone_number", "password1", "password2")},
        ),
    )
    ordering = ("id",)
    filter_horizontal = (
        "groups",
        "user_permissions",
    )


class CustomOutstandingTokenAdmin(OutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.register(User, UserAdmin)
admin.site.unregister(OutstandingToken)
admin.site.register(OutstandingToken, CustomOutstandingTokenAdmin)