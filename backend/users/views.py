from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from recipes.models import Recipe
from api.serializers import SmallRecipeSerializer
from .models import Follow
from .serializers import CustomUserSerializer, SubscriptionSerializer

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()

    @action(detail=False, permission_classes=[IsAuthenticated],)
    def subscriptions(self, request):
        user = self.request.user
        queryset = user.follower.all()
        subscriptions = [item.following for item in queryset]
        serializer = SubscriptionSerializer(
            subscriptions,
            many=True,
            context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)
        # recipes_limit = self.request.query_params.get("recipes_limit")
        # print(self.request.user.following)
        # print(self.request.user.follower)
        # subscriptions = Follow.objects.filter(user=self.request.user).all()
        # print(subscriptions)
        # recipes = Recipe.objects.filter(author=self.request.user)
        # if recipes_limit:
        #     recipes = recipes[::int(recipes_limit)]
        # serializer = CustomUserSerializer(subscriptions, many=True)
        # serializer.data["recipes"] = [SmallRecipeSerializer(recipe) for recipe in recipes]
        # print(serializer)
        # return Response(serializer.data, status=status.HTTP_200_OK)

    @action(detail=True, methods=["post", "delete"], permission_classes=[IsAuthenticated],)
    def subscribe(self, request, id=None):
        user = self.request.user
        try:
            author = get_object_or_404(User, id=id)
        except Exception:
            return Response(
                {"errors": ("Такого пользователя не существует. " +
                            "Проверьте, что передали правильный id.")},
                status=status.HTTP_400_BAD_REQUEST
            )
        if user.id == author.id:
            return Response(
                    {"errors": ("Нельзя подписаться/отписаться. Проверьте, " +
                                "что передали id, отличный от собственного.")},
                    status=status.HTTP_400_BAD_REQUEST
                )
        is_subscribed = Follow.objects.filter(user=user, following=author).exists()
        if request.method == "POST":
            if is_subscribed:
                return Response(
                    {"errors": "Вы уже подписаны на этого пользователя."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            Follow.objects.create(user=user, following=author)
            serializer = SubscriptionSerializer(author, context={"request": request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if not is_subscribed:
            return Response(
                {"errors": "Вы не были подписаны на этого пользователя."},
                status=status.HTTP_400_BAD_REQUEST
            )
        Follow.objects.filter(user=user, following=author).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
