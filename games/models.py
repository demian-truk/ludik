from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class Game(models.Model):
    name = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Название"
    )
    slug = models.CharField(
        max_length=255,
        unique=True,
        db_index=True,
        blank=True,
        null=True,
        verbose_name="Slug",
    )
    content = models.TextField(blank=True, null=True, verbose_name="Описание")
    image = models.ImageField(
        upload_to="games/%Y/%m/%d/", blank=True, null=True, verbose_name="Изображение"
    )
    release_date = models.DateField(blank=True, null=True, verbose_name="Дата выхода")
    developer = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Разработчик"
    )
    publisher = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="Издатель"
    )
    trailer_url = models.URLField(
        blank=True, null=True, verbose_name="Ссылка на трейлер"
    )
    stopgame_rating = models.DecimalField(
        blank=True,
        null=True,
        decimal_places=1,
        max_digits=3,
        verbose_name="StopGame рейтинг",
    )
    stopgame_link = models.URLField(blank=True, null=True, verbose_name="StopGame URL")
    publication_status = models.BooleanField(
        default=False, verbose_name="Публикация на сайте"
    )
    tags = TaggableManager(blank=True, verbose_name="Теги")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("show_game", kwargs={"game_slug": self.slug})

    class Meta:
        verbose_name = "Игра"
        verbose_name_plural = "Игры"
        ordering = ["-release_date"]
