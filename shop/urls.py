from django.urls import path

from .views import (
    ProductsList,
    ShowProduct,
    ShowProductsCategories
)

urlpatterns = [
    path("products/", ProductsList.as_view(), name="products"),
    path("products/<slug:product_slug>/", ShowProduct.as_view(), name="show_product"),
    path(
        "products/categories/<slug:category_slug>/",
        ShowProductsCategories.as_view(),
        name="products_categories",
    ),
]
