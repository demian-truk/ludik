# Generated by Django 4.1.2 on 2022-11-17 20:17

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="NewsCategory",
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
                "verbose_name": "Категория новостей",
                "verbose_name_plural": "Категории новостей",
            },
        ),
        migrations.CreateModel(
            name="News",
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
                ("title", models.CharField(max_length=255, verbose_name="Заголовок")),
                (
                    "slug",
                    models.CharField(
                        db_index=True, max_length=255, unique=True, verbose_name="Slug"
                    ),
                ),
                ("content", models.TextField(verbose_name="Содержимое")),
                (
                    "image",
                    models.ImageField(
                        upload_to="news/%Y/%m/%d/", verbose_name="Изображение"
                    ),
                ),
                (
                    "video_url",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ссылка на видео"
                    ),
                ),
                (
                    "time_create",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Время создания"
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="news.newscategory",
                        verbose_name="Категория",
                    ),
                ),
                (
                    "tags",
                    taggit.managers.TaggableManager(
                        blank=True,
                        help_text="A comma-separated list of tags.",
                        through="taggit.TaggedItem",
                        to="taggit.Tag",
                        verbose_name="Теги",
                    ),
                ),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
                "ordering": ["-time_create"],
            },
        ),
    ]
