import django_filters

from .models import Game


class GamesFilter(django_filters.FilterSet):
    class Meta:
        model = Game
        fields = {"name": ["icontains"]}
