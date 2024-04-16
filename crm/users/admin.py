from django.contrib import admin

from users.models import Management


@admin.register(Management)
class ManagementAdmin(admin.ModelAdmin):
    list_display = "user", "name", "role"
    ordering = ["role"]
    search_fields = "name", "role"
    fieldsets = [
        (None, {
            "fields": ("name",)
        }),
        ("Role", {
            "fields": ("role",),
            "classes": ("wide",),
        })
    ]
