from django.contrib.auth.models import User
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


class CartProduct(models.Model):
    cart = models.ForeignKey(
        "Cart",
        on_delete=models.CASCADE,
        related_name="related_products",
        verbose_name="Корзина",
    )
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Товар")
    quantity = models.PositiveIntegerField(default=1, verbose_name="Количество")
    total_price = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name="Итоговая цена"
    )

    def __str__(self):
        return "{} (для корзины №{})".format(self.product.name, self.cart.id)

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.product.price
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Товар для корзины"
        verbose_name_plural = "Товары для корзины"


class Cart(models.Model):
    user = models.ForeignKey(
        "Customer", null=True, on_delete=models.CASCADE, verbose_name="Покупатель"
    )
    products = models.ManyToManyField(
        CartProduct, related_name="related_cart", verbose_name="Товары"
    )
    in_order = models.BooleanField(default=False, verbose_name="В заказе")
    for_anonymous_user = models.BooleanField(
        default=False, verbose_name="Анонимный пользователь"
    )
    total_price = models.DecimalField(
        max_digits=8, default=0, decimal_places=2, verbose_name="Итоговая цена"
    )

    def __str__(self):
        return "Корзина №{}".format(self.id)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "Корзины"


class Customer(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    phone = models.CharField(
        max_length=20, null=True, blank=True, verbose_name="Номер телефона"
    )
    address = models.CharField(
        max_length=255, null=True, blank=True, verbose_name="Адрес"
    )
    orders = models.ManyToManyField(
        "Order", related_name="related_customer", verbose_name="Заказы покупателя"
    )

    def __str__(self):
        return "{}".format(self.user)

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Order(models.Model):
    STATUS_NEW = "new"
    STATUS_IN_PROGRESS = "in_progress"
    STATUS_COMPLETED = "completed"

    STATUS_CHOICES = (
        (STATUS_NEW, "Новый заказ"),
        (STATUS_IN_PROGRESS, "В обработке"),
        (STATUS_COMPLETED, "Заказ отправлен"),
    )

    cart = models.ForeignKey(
        Cart, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Корзина"
    )
    first_name = models.CharField(max_length=50, verbose_name="Имя")
    last_name = models.CharField(max_length=50, verbose_name="Фамилия")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    address = models.CharField(max_length=255, verbose_name="Адрес доставки")
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default=STATUS_NEW,
        verbose_name="Статус заказа",
    )
    comment = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="Комментарий к заказу"
    )
    time_create = models.DateTimeField(auto_now=True, verbose_name="Время создания")

    def __str__(self):
        return "Заказ №{}".format(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
