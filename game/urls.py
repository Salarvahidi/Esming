from django.urls import path, include
from rest_framework import routers

from game import views

router = routers.DefaultRouter()
router.register(r"default-fields", views.DefaultFieldViewSet)
router.register(r"rooms", views.RoomViewSet)
router.register(r"round-results", views.RoundResultViewSet)
router.register(r"game", views.GameViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
