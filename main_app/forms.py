from django import forms

from main_app.models import Comment, Feedback


class FeedbackForm(forms.ModelForm):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"placeholder": "Ваше имя", "class": "form-control"}
        ),
    )
    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput(
            attrs={"placeholder": "Электронная почта", "class": "form-control"}
        ),
    )
    content = forms.CharField(
        max_length=1000,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Текст сообщения",
                "cols": "60",
                "rows": "7",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Feedback
        fields = ["name", "email", "content"]


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=1000,
        label="Добавить комментарий",
        widget=forms.Textarea(attrs={"rows": "4", "class": "form-control"}),
    )

    class Meta:
        model = Comment
        fields = ["content", "news"]
