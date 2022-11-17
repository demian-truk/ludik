from django.urls import path

from .views import NewsList, ShowNews, ShowNewsCategories

urlpatterns = [
    path("news/", NewsList.as_view(), name="news"),
    path("news/<slug:news_slug>/", ShowNews.as_view(), name="show_news"),
    path(
        "news/categories/<slug:category_slug>/",
        ShowNewsCategories.as_view(),
        name="news_categories",
    ),
]
