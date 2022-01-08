from rest_framework import serializers
from apps.team.models import Team, TeamRecords


class TeamRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamRecords
        fields = [
            "wins",
            "losses",
            "ot",
            "goals_against",
            "goals_scored",
            "points",
            "games_played",
            "streak_type",
            "streak_length",
            "wild_card_rank",
        ]


class TeamListSerializer(serializers.ModelSerializer):
    record = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = ["code", "name", "city_name", "team_name", "division", "record"]

    def get_record(self, obj):
        return TeamRecordSerializer(
            obj.team_record.filter(season="20202021").first()
        ).data


class TeamDetailSerializer(TeamListSerializer):
    pass
