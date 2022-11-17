from django.contrib import admin
from django.utils.safestring import mark_safe

from news.models import News, NewsCategory


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "get_html_image", "time_create", "category")
    list_display_links = ("id", "title")
    search_fields = ("title", "category__name")
    list_filter = ("time_create",)
    prepopulated_fields = {"slug": ("title",)}
    readonly_fields = ("get_html_image",)

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=60>')

    get_html_image.short_description = "Превью"


@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
