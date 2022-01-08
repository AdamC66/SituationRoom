from django.urls import path

from django.urls import path
from apps.common.rest.api import HeartBeatViewSet

urlpatterns = [
    path('', HeartBeatViewSet.as_view({'get': 'retrieve'})),
]
