from django.urls import path

from .views import GamesList, ShowGame

urlpatterns = [
    path("games/", GamesList.as_view(), name="games"),
    path("games/<slug:game_slug>/", ShowGame.as_view(), name="show_game"),
]
