from django.urls import path

from .views import (
    AddToCartView,
    CartView,
    ChangeQuantityView,
    CheckoutView,
    DeleteFromCartView,
    MakeOrderView,
    ProductsList,
    ShowProduct,
    ShowProductsCategories,
)

urlpatterns = [
    path("products/", ProductsList.as_view(), name="products"),
    path("products/<slug:product_slug>/", ShowProduct.as_view(), name="show_product"),
    path(
        "products/categories/<slug:category_slug>/",
        ShowProductsCategories.as_view(),
        name="products_categories",
    ),
    path("cart/", CartView.as_view(), name="cart"),
    path(
        "add-to-cart/<slug:product_slug>/", AddToCartView.as_view(), name="add_to_cart"
    ),
    path(
        "remove-from-cart/<slug:product_slug>/",
        DeleteFromCartView.as_view(),
        name="delete_from_cart",
    ),
    path(
        "change-quantity/<slug:product_slug>/",
        ChangeQuantityView.as_view(),
        name="change_quantity",
    ),
    path("checkout/", CheckoutView.as_view(), name="checkout"),
    path("make-order/", MakeOrderView.as_view(), name="make_order"),
]
