from datetime import datetime

from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = (("мужской", "Мужской"), ("женский", "Женский"))


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, verbose_name="Пользователь"
    )
    date_joined = models.DateTimeField(
        default=datetime.now, verbose_name="Дата регистрации"
    )
    date_of_birth = models.DateField(
        blank=True, null=True, verbose_name="Дата рождения"
    )
    gender = models.CharField(
        max_length=25, choices=GENDER_CHOICES, blank=True, null=True, verbose_name="Пол"
    )
    photo = models.ImageField(
        upload_to="users/%Y/%m/%d", blank=True, null=True, verbose_name="Аватар"
    )
    bio = models.TextField(
        max_length=1000, blank=True, null=True, verbose_name="О себе"
    )

    def __str__(self):
        return "Профиль пользователя: {}".format(self.user.username)

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"
        ordering = ["-date_joined"]
