from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import DetailView, FormView, ListView

from main_app.forms import CommentForm
from news.models import News
from news.utils import NewsCategoryDataMixin


class NewsList(NewsCategoryDataMixin, ListView):
    model = News
    template_name = "news/news.html"
    context_object_name = "news"

    def get_queryset(self):
        return News.objects.filter().select_related("category")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Новости")
        return dict(list(context.items()) + list(c_def.items()))


class ShowNews(DetailView, FormView):
    model = News
    template_name = "news/show_news.html"
    slug_url_kwarg = "news_slug"
    context_object_name = "news"
    form_class = CommentForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = context["news"]
        return dict(list(context.items()))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            messages.success(request, "Ваш комментарий отправлен на проверку")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "Ошибка добавления комментария")


class ShowNewsCategories(NewsCategoryDataMixin, ListView):
    model = News
    template_name = "news/news.html"
    context_object_name = "news"
    allow_empty = False

    def get_queryset(self):
        return News.objects.filter(
            category__slug=self.kwargs["category_slug"]
        ).select_related("category")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(
            title=str(context["news"][0].category),
            category_selected=context["news"][0].category_id,
        )
        return dict(list(context.items()) + list(c_def.items()))
