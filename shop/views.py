from django.contrib import messages
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, ListView, View

from .forms import OrderForm
from .models import CartProduct, Customer, Product
from .utils import CartMixin, ProductsCategoryDataMixin, recalc_cart


class ProductsList(CartMixin, ProductsCategoryDataMixin, ListView):
    model = Product
    template_name = "shop/products.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter().select_related("category")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = self.cart
        c_def = self.get_user_context(title="Каталог товаров")
        return dict(list(context.items()) + list(c_def.items()))


class ShowProduct(CartMixin, DetailView):
    model = Product
    template_name = "shop/show_product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = self.cart
        context["title"] = context["product"]
        return dict(list(context.items()))


class ShowProductsCategories(CartMixin, ProductsCategoryDataMixin, ListView):
    model = Product
    template_name = "shop/products.html"
    context_object_name = "products"
    allow_empty = False

    def get_queryset(self):
        return Product.objects.filter(
            category__slug=self.kwargs["category_slug"]
        ).select_related("category")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = self.cart
        c_def = self.get_user_context(
            title=str(context["products"][0].category),
            category_selected=context["products"][0].category_id,
        )
        return dict(list(context.items()) + list(c_def.items()))


class CartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        title = "Корзина"
        context = {"cart": self.cart, "title": title}
        return render(request, "shop/cart.html", context)


class AddToCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        prod_slug = kwargs.get("product_slug")
        product = Product.objects.get(slug=prod_slug)
        cart_product, created = CartProduct.objects.get_or_create(
            cart=self.cart,
            product=product,
        )
        if created:
            self.cart.products.add(cart_product)
        recalc_cart(self.cart)
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


class DeleteFromCartView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        prod_slug = kwargs.get("product_slug")
        product = Product.objects.get(slug=prod_slug)
        cart_product = CartProduct.objects.get(
            cart=self.cart,
            product=product,
        )
        self.cart.products.remove(cart_product)
        cart_product.delete()
        recalc_cart(self.cart)
        return HttpResponseRedirect("/cart/")


class ChangeQuantityView(CartView, View):
    def post(self, request, *args, **kwargs):
        prod_slug = kwargs.get("product_slug")
        product = Product.objects.get(slug=prod_slug)
        cart_product = CartProduct.objects.get(
            cart=self.cart,
            product=product,
        )
        quantity = int(request.POST.get("quantity"))
        cart_product.quantity = quantity
        cart_product.save()
        recalc_cart(self.cart)
        return HttpResponseRedirect("/cart/")


class CheckoutView(CartMixin, View):
    def get(self, request, *args, **kwargs):
        title = "Оформление заказа"
        form = OrderForm(request.POST or None)
        context = {"cart": self.cart, "title": title, "form": form}
        return render(request, "shop/checkout.html", context)


class MakeOrderView(CartMixin, View):
    @transaction.atomic
    def post(self, request, *args, **kwargs):
        form = OrderForm(request.POST or None)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.first_name = form.cleaned_data["first_name"]
            new_order.last_name = form.cleaned_data["last_name"]
            new_order.phone = form.cleaned_data["phone"]
            new_order.address = form.cleaned_data["address"]
            new_order.comment = form.cleaned_data["comment"]
            new_order.save()
            self.cart.in_order = True
            self.cart.save()
            new_order.cart = self.cart
            new_order.save()
            messages.success(
                request,
                "Спасибо за заказ! В ближайшее время наш менеджер Отдела продаж с Вами свяжется.",
            )

            if request.user.is_authenticated:
                customer = Customer.objects.get(user=request.user)
                customer.orders.add(new_order)
            return HttpResponseRedirect("/products/")
        return HttpResponseRedirect("/checkout/")
