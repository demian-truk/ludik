from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, ProductsCategory


@admin.register(ProductsCategory)
class ProductsCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "get_html_image",
        "price",
        "stock",
        "available",
        "category",
    )
    list_display_links = ("id", "name")
    search_fields = ("name", "category__name")
    list_filter = ("available",)
    list_editable = ("price", "stock", "available")
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("get_html_image",)

    def get_html_image(self, object):
        if object.image:
            return mark_safe(f'<img src="{object.image.url}" width=60>')

    get_html_image.short_description = "Превью"
