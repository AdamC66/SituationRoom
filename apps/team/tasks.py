from celery import shared_task
from apps.team.models import Team, TeamRecords
from datetime import datetime, timedelta
from django.utils import timezone
import requests


@shared_task
def update_standings(force=False):
    should_update_standings = TeamRecords.objects.filter(
        season="20202021", last_updated__lt=timezone.now() - timedelta(days=1)
    ).exists()
    if should_update_standings or force:
        data = requests.get("https://statsapi.web.nhl.com/api/v1/standings").json()[
            "records"
        ]
        for division in data:
            for team in division["teamRecords"]:
                team_model = Team.objects.get(nhl_api_id=team["team"]["id"])
                try:  # if team already exists
                    team_record = TeamRecords.objects.get(
                        team=team_model, season="20202021"
                    )
                except TeamRecords.DoesNotExist:
                    team_record = TeamRecords(team=team_model, season="20202021")
                team_record.wins = team["leagueRecord"]["wins"]
                team_record.losses = team["leagueRecord"]["losses"]
                team_record.ot = team["leagueRecord"]["ot"]
                team_record.row = team["row"]
                team_record.goals_against = team["goalsAgainst"]
                team_record.goals_scored = team["goalsScored"]
                team_record.points = team["points"]
                team_record.games_played = team["gamesPlayed"]
                team_record.streak_type = team["streak"]["streakType"]
                team_record.streak_length = team["streak"]["streakNumber"]
                team_record.wild_card_rank = team["wildCardRank"]
                team_record.save()
        return "Standings updated - {}".format(
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    return "Standings already up to date - {}".format(
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
