from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets

from user.serializers import UserSerializer
from user.models import User


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.order_by("-date_joined")
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    ordering_fields = "__all__"
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    search_fields = [
        "first_name",
        "last_name",
        "username",
    ]
