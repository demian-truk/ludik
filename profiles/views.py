from django.contrib import messages
from django.contrib.auth import logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from profiles.forms import (
    AccountPasswordChangeForm,
    LoginUserForm,
    ProfileEditForm,
    RegisterUserForm,
    UserEditForm,
)
from profiles.models import Profile


def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.save()
            return redirect("login")
    else:
        form = RegisterUserForm()
    return render(
        request, "profiles/register.html", {"form": form, "title": "Регистрация"}
    )


class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = "profiles/login.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Авторизация"
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy("index")


def logout_user(request):
    logout(request)
    return redirect("login")


@login_required
def account_edit(request):
    if request.method == "POST":
        form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(
            instance=request.user.profile, data=request.POST, files=request.FILES
        )
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()
            messages.success(request, "Данные аккаунта успешно обновлены")
        else:
            messages.error(request, "Ошибка обновления данных аккаунта")
    else:
        form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(
        request,
        "profiles/account_edit.html",
        {
            "form": form,
            "profile_form": profile_form,
            "title": "Редактирование аккаунта",
        },
    )


class AccountPasswordChange(LoginRequiredMixin, TemplateView):
    form_class = AccountPasswordChangeForm

    def get(self, request, *args, **kwargs):
        form = self.form_class(self.request.user)
        return render(
            request,
            "profiles/account_password_change.html",
            {"form": form, "title": "Изменение пароля"},
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Пароль успешно изменен")
            return HttpResponseRedirect(request.META.get("HTTP_REFERER"))
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
                return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def account_profile(request):
    user = request.user
    return render(
        request, "profiles/account_profile.html", {"user": user, "title": "Мой профиль"}
    )


def users_list(request):
    profiles = Profile.objects.all()
    paginator = Paginator(profiles, 20)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request,
        "profiles/users_list.html",
        {"profiles": profiles, "title": "Список пользователей", "page_obj": page_obj},
    )
