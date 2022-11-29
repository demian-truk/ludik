from django.db import models
from django.db.models import Count
from django.views.generic import View

from .models import Cart, Customer, ProductsCategory


class ProductsCategoryDataMixin:
    paginate_by = 15

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = ProductsCategory.objects.annotate(Count("product"))
        context["cats"] = cats
        if "category_selected" not in context:
            context["category_selected"] = 0
        return context


class CartMixin(View):
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            customer = Customer.objects.filter(user=request.user).first()
            if not customer:
                customer = Customer.objects.create(user=request.user)
            cart = Cart.objects.filter(user=customer, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(user=customer)
        else:
            cart = Cart.objects.filter(for_anonymous_user=True, in_order=False).first()
            if not cart:
                cart = Cart.objects.create(for_anonymous_user=True)
        self.cart = cart
        return super().dispatch(request, *args, **kwargs)


def recalc_cart(cart):
    cart_data = cart.products.aggregate(models.Sum("total_price"))
    if cart_data.get("total_price__sum"):
        cart.total_price = cart_data["total_price__sum"]
    else:
        cart.total_price = 0
    cart.save()
