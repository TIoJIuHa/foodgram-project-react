from django.contrib.auth import get_user_model
from djoser.views import UserViewSet
from rest_framework import status, viewsets
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

User = get_user_model()


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()

    @action(detail=False, permission_classes=[IsAuthenticated],)
    def subscriptions(self, request):
        pass

    @action(detail=False, methods=["post", "delete"], permission_classes=[IsAuthenticated],)
    def subscribe(self, request):
        pass
