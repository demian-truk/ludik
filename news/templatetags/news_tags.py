from django import template
from django.db.models import Count

from news.models import News

register = template.Library()


@register.simple_tag()
def get_most_commented_news(count=1):
    return News.objects.annotate(total_comments=Count("comments_news")).order_by(
        "-total_comments"
    )[:count]
