from apps.team.models import Team
from apps.team.rest.serializers import TeamListSerializer, TeamDetailSerializer
from situationroom.views import GenericGetAndListAPIView
from apps.team.tasks import update_standings


class TeamViewSet(GenericGetAndListAPIView):
    queryset = Team.objects.all()
    lookup_field = "code"
    lookup_url_kwarg = "team_code"
    detail_read_serializer = TeamDetailSerializer
    list_read_serializer = TeamListSerializer

    def list(self, request, *args, **kwargs):
        # TODO FIX REDIS
        # x = update_standings.delay()
        return super().list(request, *args, **kwargs)
