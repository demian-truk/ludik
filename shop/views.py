from django.views.generic import DetailView, ListView

from .models import Product
from .utils import ProductsCategoryDataMixin


class ProductsList(ProductsCategoryDataMixin, ListView):
    model = Product
    template_name = "shop/products.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.filter().select_related("category")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Каталог товаров")
        return dict(list(context.items()) + list(c_def.items()))


class ShowProduct(DetailView):
    model = Product
    template_name = "shop/show_product.html"
    slug_url_kwarg = "product_slug"
    context_object_name = "product"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["product"]
        return dict(list(context.items()))


class ShowProductsCategories(ProductsCategoryDataMixin, ListView):
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
        c_def = self.get_user_context(
            title=str(context["products"][0].category),
            category_selected=context["products"][0].category_id,
        )
        return dict(list(context.items()) + list(c_def.items()))
