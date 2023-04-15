from django.contrib.auth import get_user_model
from django_filters import ModelMultipleChoiceFilter
from django_filters import rest_framework as django_filters

from recipes.models import Recipe, Tag

from rest_framework import filters

User = get_user_model()


class RecipeFilter(django_filters.FilterSet):
    author = django_filters.filters.ModelChoiceFilter(
        queryset=User.objects.all()
    )
    tags = ModelMultipleChoiceFilter(
        field_name="tags__slug",
        to_field_name="slug",
        queryset=Tag.objects.all()
    )
    is_favorited = django_filters.filters.BooleanFilter(
        method="filter_favorited"
    )
    is_in_shopping_cart = django_filters.filters.BooleanFilter(
        method="filter_shopping_cart"
    )

    def filter_favorited(self, queryset, name, value):
        if value:
            return queryset.filter(favorite__user=self.request.user)
        return queryset

    def filter_shopping_cart(self, queryset, name, value):
        if value:
            return queryset.filter(shoppingcart__user=self.request.user)
        return queryset

    class Meta:
        model = Recipe
        fields = ("tags", "author", "is_favorited", "is_in_shopping_cart")


class IngredientSearchFilter(filters.SearchFilter):
    search_param = "name"
