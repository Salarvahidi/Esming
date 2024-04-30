from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from landing.views import home

admin.site.site_header = "Esming Admin"
admin.site.site_title = "Esming Admin Portal"
admin.site.index_title = "Esming Admin Portal"

api_urlpatterns = [
    path("user/", include("user.urls"), name="user"),
    path("game/", include("game.urls"), name="game"),
]

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_urlpatterns)),
    path("home/", home),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static("home/", document_root="landing/images/")
