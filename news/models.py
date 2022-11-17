from django.db import models
from django.urls import reverse
from taggit.managers import TaggableManager


class News(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.CharField(
        max_length=255, unique=True, db_index=True, verbose_name="Slug"
    )
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="news/%Y/%m/%d/", verbose_name="Изображение")
    video_url = models.URLField(blank=True, null=True, verbose_name="Ссылка на видео")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    category = models.ForeignKey(
        "NewsCategory", on_delete=models.PROTECT, verbose_name="Категория"
    )
    tags = TaggableManager(blank=True, verbose_name="Теги")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("show_news", kwargs={"news_slug": self.slug})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-time_create"]


class NewsCategory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    slug = models.CharField(
        max_length=50, unique=True, db_index=True, verbose_name="Slug"
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("news_categories", kwargs={"category_slug": self.slug})

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"
