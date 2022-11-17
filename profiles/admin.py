from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "get_html_photo", "date_joined", "gender"]
    list_display_links = ("id", "user")
    search_fields = ("user__username",)
    list_filter = ("date_joined",)
    readonly_fields = ("get_html_photo",)
    raw_id_fields = ("user",)

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f'<img src="{object.photo.url}" width=60>')

    get_html_photo.short_description = "Аватар"
