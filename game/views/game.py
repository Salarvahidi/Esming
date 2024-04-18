from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from game.serializers import GameSerializer
from game.models import Game


class GameViewSet(viewsets.ModelViewSet):

    queryset = Game.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = "__all__"
    permission_classes = [IsAuthenticated]
    serializer_class = GameSerializer

    search_fields = [
        "id",
    ]
