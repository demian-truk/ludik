from django import forms
from django.contrib.auth.forms import (
    AuthenticationForm,
    PasswordChangeForm,
    UserCreationForm,
)
from django.contrib.auth.models import User

from .models import GENDER_CHOICES, Profile


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите логин", "class": "form-control"}
        ),
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Введите пароль", "class": "form-control"}
        ),
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Повторите пароль", "class": "form-control"}
        ),
    )

    class Meta:
        model = User
        fields = ("username", "password1", "password2")


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Введите логин", "class": "form-control"}
        ),
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"placeholder": "Введите пароль", "class": "form-control"}
        ),
    )


class UserEditForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Ваше красивое имя", "class": "form-control"}
        ),
        label="Имя",
        required=False,
    )
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={"placeholder": "Ваша прекрасная фамилия", "class": "form-control"}
        ),
        label="Фамилия",
        required=False,
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={"placeholder": "example@email.com", "class": "form-control"}
        ),
        label="Электронная почта",
        required=False,
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")


class ProfileEditForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        label="Дата рождения",
        required=False,
    )
    gender = forms.ChoiceField(
        choices=GENDER_CHOICES,
        widget=forms.Select(attrs={"class": "form-control"}),
        label="Пол",
        required=False,
    )
    photo = forms.FileField(
        widget=forms.FileInput(attrs={"class": "form-control"}),
        label="Аватар",
        required=False,
    )
    bio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Здесь могло быть Ваше описание самого себя, "
                "но пока Вы слишком заняты, чтобы уделить этому время",
                "class": "form-control",
                "cols": "60",
                "rows": "7",
            }
        ),
        label="О себе",
        required=False,
    )

    class Meta:
        model = Profile
        fields = ("date_of_birth", "gender", "photo", "bio")


class AccountPasswordChangeForm(PasswordChangeForm):
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(user, *args, **kwargs)
        self.fields["old_password"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите старый пароль",
            }
        )
        self.fields["new_password1"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Введите новый пароль",
            }
        )
        self.fields["new_password2"].widget.attrs.update(
            {
                "class": "form-control",
                "placeholder": "Повторите новый пароль",
            }
        )

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user
