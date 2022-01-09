from apps.player.models import Player
from apps.player.rest.serializers import PlayerListSerializer, PlayerDetailSerializer
from situationroom.views import GenericGetAndListAPIView
from rest_framework import pagination


class StandardResultsSetPagination(pagination.PageNumberPagination):
    page_size = 100
    page_size_query_param = "page_size"
    max_page_size = 100


class PlayerViewSet(GenericGetAndListAPIView):
    pagination_class = StandardResultsSetPagination
    queryset = Player.objects.all()
    lookup_field = "pk"
    lookup_url_kwarg = "player_code"
    detail_read_serializer = PlayerDetailSerializer
    list_read_serializer = PlayerListSerializer
