from baseapp import models
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

my_models = [
    models.Assessment,
    models.AssessmentGroup,
    models.Question,
    models.Answer,
    models.Tag,
]


class UserAdmin(BaseUserAdmin):
    """Define the admin page for User."""

    ordering = ["id"]
    list_display = [
        "email",
        "name",
    ]
    # fieldsets: What fields will be shown when editing a user.
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "name",
                    "email",
                    "password",
                )
            },
        ),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_teacher",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),  # css class
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "name",
                    "is_teacher",
                    "is_staff",
                    "is_superuser",
                    "is_active",
                ),
            },
        ),
    )


admin.site.register(models.User, UserAdmin)

for model in my_models:
    admin.site.register(model)
