from django.conf.urls.static import static
from django.urls import re_path, path
from apps.player.rest.api import PlayerViewSet

urlpatterns = [
    path("players/", PlayerViewSet.as_view()),
    re_path("^players/(?P<player_code>\w+|)/$", PlayerViewSet.as_view()),
]
