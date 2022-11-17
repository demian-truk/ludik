from django.urls import path

from .views import FeedbackFormView, about, index, rules

urlpatterns = [
    path("", index, name="index"),
    path("about/", about, name="about"),
    path("feedback/", FeedbackFormView.as_view(), name="feedback"),
    path("rules/", rules, name="rules"),
]
