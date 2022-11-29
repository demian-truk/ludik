from django.db import models
from django.urls import reverse


class ProductsCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name="Slug"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("products_categories", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Категория товаров"
        verbose_name_plural = "Категории товаров"
        ordering = ["name"]


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    slug = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name="Slug"
    )
    category = models.ForeignKey(
        ProductsCategory, on_delete=models.PROTECT, verbose_name="Категория"
    )
    image = models.ImageField(
        upload_to="products/%Y/%m/%d/", verbose_name="Изображение"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name="Цена")
    stock = models.PositiveIntegerField(verbose_name="Остаток товара")
    available = models.BooleanField(default=True, verbose_name="Доступность товара")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_product", kwargs={"product_slug": self.slug})

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ["name"]
