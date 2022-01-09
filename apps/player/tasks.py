from celery import shared_task
from apps.team.models import Team, TeamRecords
from apps.player.models import Player, PlayerStats
from datetime import datetime, timedelta
from django.utils import timezone
import requests
import time


@shared_task
def update_all_team_rosters():
    all_teams = Team.objects.all()
    for team in all_teams:
        roster_data = requests.get(
            f"https://statsapi.web.nhl.com/api/v1/teams/{team.nhl_api_id}/roster"
        ).json()
        results = []
        for person in roster_data["roster"]:
            try:
                player = Player.objects.get(nhl_api_id=person["person"]["id"])
                player.current_team = team
                player.full_name = person["person"]["fullName"]
                player.jersey_number = person["jerseyNumber"]
                player.position_code = person["position"]["code"]
                player.position_name = person["position"]["name"]
                player.position_type = person["position"]["type"]
                player.position_abbv = person["position"]["abbreviation"]
                player.save()
            except Player.DoesNotExist:
                player = Player.objects.create(
                    full_name=person["person"]["fullName"],
                    nhl_api_id=person["person"]["id"],
                    jersey_number=person["jerseyNumber"],
                    position_code=person["position"]["code"],
                    position_name=person["position"]["name"],
                    position_type=person["position"]["type"],
                    position_abbv=person["position"]["abbreviation"],
                    current_team=team,
                )
                player.save()
            results.append(
                {"player": player.full_name, "team": team.name, "id": player.nhl_api_id}
            )


@shared_task
def update_team_roster(team_code):
    team = Team.objects.get(code=team_code)
    roster_data = requests.get(
        f"https://statsapi.web.nhl.com/api/v1/teams/{team.nhl_api_id}/roster"
    ).json()
    results = []
    for person in roster_data["roster"]:
        try:
            player = Player.objects.get(nhl_api_id=person["person"]["id"])
            player.current_team = team
            player.full_name = person["person"]["fullName"]
            player.jersey_number = person["jerseyNumber"]
            player.position_code = person["position"]["code"]
            player.position_name = person["position"]["name"]
            player.position_type = person["position"]["type"]
            player.position_abbv = person["position"]["abbreviation"]
            player.save()
        except Player.DoesNotExist:
            player = Player.objects.create(
                full_name=person["person"]["fullName"],
                nhl_api_id=person["person"]["id"],
                jersey_number=person["jerseyNumber"],
                position_code=person["position"]["code"],
                position_name=person["position"]["name"],
                position_type=person["position"]["type"],
                position_abbv=person["position"]["abbreviation"],
                current_team=team,
            )
            player.save()
        results.append(
            {"player": player.full_name, "team": team.name, "id": player.nhl_api_id}
        )
    return results


@shared_task
def update_advanced_player_data(player_id):
    player = Player.objects.get(pk=player_id)
    nhl_data = requests.get(
        f"https://statsapi.web.nhl.com/api/v1/people/{player.nhl_api_id}"
    ).json()

    player.first_name = nhl_data["people"][0]["firstName"]
    player.last_name = nhl_data["people"][0]["lastName"]
    player.birth_date = nhl_data["people"][0]["birthDate"]
    player.current_age = nhl_data["people"][0]["currentAge"]
    player.birth_city = nhl_data["people"][0]["birthCity"]
    if "birthStateProvince" in nhl_data["people"][0]:
        player.birth_state_province = nhl_data["people"][0]["birthStateProvince"]
    player.birth_country = nhl_data["people"][0]["birthCountry"]
    player.nationality = nhl_data["people"][0]["nationality"]
    player.height = nhl_data["people"][0]["height"]
    player.weight = nhl_data["people"][0]["weight"]
    player.active = nhl_data["people"][0]["active"]
    player.alternate_captain = nhl_data["people"][0]["alternateCaptain"]
    player.captain = nhl_data["people"][0]["captain"]
    player.shoots_catches = nhl_data["people"][0]["shootsCatches"]
    player.roster_status = nhl_data["people"][0]["rosterStatus"]
    player.rookie = nhl_data["people"][0]["rookie"]
    player.save()
    return player


@shared_task
def update_full_team_player_data(team_code):
    players = Player.objects.filter(current_team__code=team_code)
    results = []
    for player in players:
        updated_player = update_advanced_player_data(player.id)
        time.sleep(3)
        results.append(
            {
                "player": updated_player.full_name,
                "team": updated_player.current_team.name,
                "id": updated_player.nhl_api_id,
            }
        )
    return results
