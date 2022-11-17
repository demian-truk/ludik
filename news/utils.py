from django.db.models import Count

from .models import NewsCategory


class NewsCategoryDataMixin:
    paginate_by = 15

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = NewsCategory.objects.annotate(Count("news"))
        context["cats"] = cats
        if "category_selected" not in context:
            context["category_selected"] = 0
        return context
