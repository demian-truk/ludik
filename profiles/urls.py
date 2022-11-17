from django.urls import path

from profiles.views import (
    AccountPasswordChange,
    LoginUser,
    account_edit,
    account_profile,
    logout_user,
    register_user,
    users_list,
)

urlpatterns = [
    path("register/", register_user, name="register"),
    path("login/", LoginUser.as_view(), name="login"),
    path("logout/", logout_user, name="logout"),
    path("account/profile/", account_profile, name="account_profile"),
    path("account/edit/", account_edit, name="account_edit"),
    path(
        "account/password-change/",
        AccountPasswordChange.as_view(),
        name="account_password_change",
    ),
    path("users/", users_list, name="users_list"),
]
