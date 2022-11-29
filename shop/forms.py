from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    first_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"placeholder": "Ваше имя", "class": "form-control"}
        ),
        label="Имя*",
    )
    last_name = forms.CharField(
        max_length=50,
        widget=forms.TextInput(
            attrs={"placeholder": "Ваша фамилия", "class": "form-control"}
        ),
        label="Фамилия*",
    )
    phone = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={"placeholder": "+ 375 (29) 123-45-67", "class": "form-control"}
        ),
        label="Номер телефона*",
    )
    address = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Индекс, населенный пункт, улица, дом, корпус, квартира/офис",
                "class": "form-control",
            }
        ),
        label="Адрес доставки*",
    )
    comment = forms.CharField(
        max_length=500,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Здесь Вы можете оставить любую информацию для Отдела продаж",
                "class": "form-control",
                "rows": "4",
            }
        ),
        label="Комментарий к заказу",
        required=False,
    )

    class Meta:
        model = Order
        fields = ("first_name", "last_name", "phone", "address", "comment")
