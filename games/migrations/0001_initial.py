# Generated by Django 4.1.2 on 2022-11-17 20:17

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("taggit", "0005_auto_20220424_2025"),
    ]

    operations = [
        migrations.CreateModel(
            name="Game",
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
                (
                    "name",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Название"
                    ),
                ),
                (
                    "slug",
                    models.CharField(
                        blank=True,
                        db_index=True,
                        max_length=255,
                        null=True,
                        unique=True,
                        verbose_name="Slug",
                    ),
                ),
                (
                    "content",
                    models.TextField(blank=True, null=True, verbose_name="Описание"),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="games/%Y/%m/%d/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "release_date",
                    models.DateField(blank=True, null=True, verbose_name="Дата выхода"),
                ),
                (
                    "developer",
                    models.CharField(
                        blank=True,
                        max_length=255,
                        null=True,
                        verbose_name="Разработчик",
                    ),
                ),
                (
                    "publisher",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="Издатель"
                    ),
                ),
                (
                    "trailer_url",
                    models.URLField(
                        blank=True, null=True, verbose_name="Ссылка на трейлер"
                    ),
                ),
                (
                    "stopgame_rating",
                    models.DecimalField(
                        blank=True,
                        decimal_places=1,
                        max_digits=3,
                        null=True,
                        verbose_name="StopGame рейтинг",
                    ),
                ),
                (
                    "stopgame_link",
                    models.URLField(blank=True, null=True, verbose_name="StopGame URL"),
                ),
                (
                    "publication_status",
                    models.BooleanField(
                        default=False, verbose_name="Публикация на сайте"
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
                "verbose_name": "Игра",
                "verbose_name_plural": "Игры",
                "ordering": ["-release_date"],
            },
        ),
    ]