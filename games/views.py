from django.views.generic import DetailView, ListView

from .filters import GamesFilter
from .models import Game


class GamesList(ListView):
    model = Game
    template_name = "games/games.html"
    context_object_name = "games"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = GamesFilter(self.request.GET, queryset=self.get_queryset())
        context["title"] = "Игры"
        return dict(list(context.items()))


class ShowGame(DetailView):
    model = Game
    template_name = "games/show_game.html"
    slug_url_kwarg = "game_slug"
    context_object_name = "game"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["game"]
        return dict(list(context.items()))
