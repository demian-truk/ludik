from django.contrib.auth.models import User
from django.db import models

from news.models import News


class Feedback(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    email = models.EmailField(verbose_name="Электронная почта")
    content = models.TextField(max_length=1000, verbose_name="Текст обращения")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return "Обращение пользователя: {}".format(self.email)

    class Meta:
        verbose_name = "Обращение"
        verbose_name_plural = "Обратная связь"
        ordering = ["-time_create"]


class Comment(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Автор комментария"
    )
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        related_name="comments_news",
        verbose_name="Заголовок новости",
    )
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    content = models.TextField(max_length=1000, verbose_name="Содержимое")
    publication_status = models.BooleanField(
        default=False, verbose_name="Публикация на сайте"
    )

    def __str__(self):
        return "Комментарий пользователя: {}".format(self.user)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-time_create"]
