from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from game.serializers import RoomSerializer
from game.models import Room


class RoomViewSet(viewsets.ModelViewSet):

    queryset = Room.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = "__all__"
    permission_classes = [IsAuthenticated]
    serializer_class = RoomSerializer

    search_fields = ["id", "room_name"]
