from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import FormView

from .forms import FeedbackForm
from .models import Feedback


def index(request):
    return render(request, "main_app/index.html", {"title": "Ludik — портал про игры"})


def about(request):
    return render(request, "main_app/about.html", {"title": "О сайте"})


class FeedbackFormView(FormView):
    model = Feedback
    template_name = "main_app/feedback.html"
    form_class = FeedbackForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Обратная связь"
        return dict(list(context.items()))

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            messages.success(request, "Ваше сообщение отправлено")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            messages.error(request, "Ошибка отправки сообщения")

        return render(request, self.template_name, self.get_context_data())


def rules(request):
    return render(
        request, "main_app/rules.html", {"title": "Соглашение о пользовании сайтом"}
    )


def page_not_found(request, exception):
    return render(
        request, "main_app/page_not_found.html", {"title": "Страница не найдена"}
    )
