from rest_framework import serializers
from apps.player.models import Player, PlayerStats


class PlayerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            "id",
            "full_name",
            "jersey_number",
            "position_code",
            "position_abbv",
            "captain",
            "alternate_captain",
            "shoots_catches",
        ]


class PlayerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Player
        fields = [
            "id",
            "full_name",
            "jersey_number",
            "position_code",
            "position_abbv",
            "captain",
            "alternate_captain",
            "birth_date",
            "birth_city",
            "birth_state_province",
            "birth_country",
            "nationality",
            "weight",
            "height",
        ]
