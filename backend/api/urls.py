from django.urls import include, path
from rest_framework.routers import DefaultRouter

from users.views import CustomUserViewSet

from .views import IngredientViewSet, RecipeViewSet, TagViewSet

router = DefaultRouter()

router.register(r"recipes", RecipeViewSet, basename="recipes")
router.register(r"tags", TagViewSet, basename="tags")
router.register(r"ingredients", IngredientViewSet, basename="ingredients")
router.register(r"users", CustomUserViewSet, basename="users")

urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path("", include(router.urls)),
]
