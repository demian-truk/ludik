from django.contrib import admin

from .models import Comment, Feedback


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "content", "time_create")
    list_display_links = ("id", "name")
    search_fields = ("name", "email", "content")
    list_filter = ("time_create",)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "news",
        "user",
        "time_create",
        "content",
        "publication_status",
    )
    list_display_links = ("id", "news")
    list_editable = ("publication_status",)
    search_fields = ("news__title", "user__username", "content")
    list_filter = ("time_create", "publication_status")
    raw_id_fields = ("user",)
