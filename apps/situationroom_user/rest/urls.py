from django.urls import path, include

from django.conf.urls.static import static
from django.urls import re_path, path
from apps.situationroom_user.rest.api import SituationRoomUserViewSet

urlpatterns = [
    path('user/', SituationRoomUserViewSet.as_view()),
]
