from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Cart, CartProduct, Customer, Order, Product, ProductsCategory


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


@admin.register(CartProduct)
class CartProductAdmin(admin.ModelAdmin):
    list_display = ("id", "product", "cart")
    list_display_links = ("id", "product")


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "in_order", "for_anonymous_user")
    list_display_links = ("id", "user")
    search_fields = ("user__username",)
    list_filter = ("in_order", "for_anonymous_user")


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "phone", "address")
    list_display_links = ("id", "user")
    search_fields = ("user__username",)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "first_name",
        "last_name",
        "phone",
        "address",
        "time_create",
        "status",
    )
    list_display_links = ("id", "first_name", "last_name")
    search_fields = ("first_name", "last_name", "phone", "address")
    list_filter = ("status", "time_create")
    list_editable = ("status",)
