from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_html_image",
        "release_date",
        "developer",
        "publication_status",
    )
    list_display_links = ("id", "name")
    search_fields = ("name", "developer")
    list_filter = ("publication_status",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("get_html_image",)

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=60>')

    get_html_image.short_description = "Превью"
