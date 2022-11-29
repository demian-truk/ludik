# Generated by Django 4.1.2 on 2022-11-29 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ProductsCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50, verbose_name="Название")),
                (
                    "slug",
                    models.CharField(
                        db_index=True, max_length=50, unique=True, verbose_name="Slug"
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория товаров",
                "verbose_name_plural": "Категории товаров",
                "ordering": ["name"],
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=255, verbose_name="Наименование")),
                (
                    "slug",
                    models.CharField(
                        db_index=True, max_length=255, unique=True, verbose_name="Slug"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        upload_to="products/%Y/%m/%d/", verbose_name="Изображение"
                    ),
                ),
                ("description", models.TextField(blank=True, verbose_name="Описание")),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=7, verbose_name="Цена"
                    ),
                ),
                ("stock", models.PositiveIntegerField(verbose_name="Остаток товара")),
                (
                    "available",
                    models.BooleanField(
                        default=True, verbose_name="Доступность товара"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shop.productscategory",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Товар",
                "verbose_name_plural": "Товары",
                "ordering": ["name"],
            },
        ),
    ]
