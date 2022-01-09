from django.conf.urls.static import static
from django.urls import re_path, path, include
from apps.team.rest.api import TeamViewSet

urlpatterns = [
    path("teams/", TeamViewSet.as_view()),
    re_path("^teams/(?P<team_code>\w+|)/$", TeamViewSet.as_view()),
]
