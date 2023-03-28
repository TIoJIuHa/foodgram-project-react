from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from recipes.models import Recipe, Tag, Ingredient
from .serializers import RecipeSerializer, TagSerializer, IngredientSerializer


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    @action(permission_classes=[IsAuthenticated],)
    def download_shopping_cart(self, request):
        pass

    @action(methods=["post", "delete"], permission_classes=[IsAuthenticated],)
    def shopping_cart(self, request):
        # serializer = self.get_serializer(request.user)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        pass

    @action(methods=["post", "delete"], permission_classes=[IsAuthenticated],)
    def favourite(self, request):
        pass


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    # + поиск по имени
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
