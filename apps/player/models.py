from django.db import models
from apps.team.models import Team

# Create your models here.
class Player(models.Model):
    POS_CHOICES = (
        ("Forward", "Forward"),
        ("Defenceman", "Defenceman"),
        ("Goalie", "Goalie"),
    )
    full_name = models.CharField(max_length=255)
    nhl_api_id = models.IntegerField()
    jersey_number = models.IntegerField()
    position_code = models.CharField(max_length=1)
    position_name = models.CharField(max_length=31)
    position_type = models.CharField(max_length=31, choices=POS_CHOICES)
    position_abbv = models.CharField(max_length=3)
    current_team = models.ForeignKey(
        Team, on_delete=models.SET_NULL, null=True, related_name="players"
    )

    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.CharField(max_length=255, null=True, blank=True)
    current_age = models.IntegerField(null=True, blank=True)
    birth_city = models.CharField(max_length=255, null=True, blank=True)
    birth_state_province = models.CharField(max_length=255, null=True, blank=True)
    birth_country = models.CharField(max_length=255, null=True, blank=True)
    nationality = models.CharField(max_length=255, null=True, blank=True)
    height = models.CharField(max_length=255, null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    active = models.BooleanField(null=True, blank=True)
    alternate_captain = models.BooleanField(null=True, blank=True)
    captain = models.BooleanField(null=True, blank=True)
    rookie = models.BooleanField(null=True, blank=True)
    shoots_catches = models.CharField(max_length=5, null=True, blank=True)
    roster_status = models.CharField(max_length=5, null=True, blank=True)

    def __str__(self):
        return f"{self.full_name}, {self.current_team.name}"


class PlayerStats(models.Model):
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, related_name="statline"
    )
    season = models.CharField(max_length=10)
    toi = models.CharField(max_length=20)
    last_updated = models.DateTimeField(auto_now_add=True, null=True)

    ##Player Stats
    assists = models.IntegerField(blank=True, null=True)
    goals = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    pim = models.IntegerField(blank=True, null=True)
    shots = models.IntegerField(blank=True, null=True)
    games = models.IntegerField(blank=True, null=True)
    hits = models.IntegerField(blank=True, null=True)
    pp_goals = models.IntegerField(blank=True, null=True)  # Powerplay goals
    pp_pts = models.IntegerField(blank=True, null=True)  # Powerplay points
    pp_toi = models.CharField(max_length=20, blank=True, null=True)
    ev_toi = models.CharField(max_length=20, blank=True, null=True)
    face_off_pct = models.FloatField(blank=True, null=True)
    shot_pct = models.FloatField(blank=True, null=True)
    gwg = models.IntegerField(blank=True, null=True)  # Game winning goals
    ot_goals = models.IntegerField(blank=True, null=True)
    sh_goals = models.IntegerField(blank=True, null=True)
    sh_points = models.IntegerField(blank=True, null=True)
    sh_toi = models.CharField(max_length=20, blank=True, null=True)
    blocked_shots = models.IntegerField(blank=True, null=True)
    plus_minus = models.IntegerField(blank=True, null=True)
    shifts = models.IntegerField(blank=True, null=True)
    toi_per_gm = models.CharField(
        max_length=20, blank=True, null=True
    )  # Average Time on ice per game
    ev_toi_per_gm = models.CharField(
        max_length=20, blank=True, null=True
    )  # Average even strength Time on ice per game
    sh_toi_per_gm = models.CharField(
        max_length=20, blank=True, null=True
    )  # Average short handed Time on ice per game
    pp_toi_per_gm = models.CharField(
        max_length=20, blank=True, null=True
    )  # Average powerplay Time on ice per game

    ##Goalie Stats
    ot = models.IntegerField(blank=True, null=True)
    shutouts = models.IntegerField(blank=True, null=True)
    ties = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)
    saves = models.IntegerField(blank=True, null=True)
    pp_saves = models.IntegerField(blank=True, null=True)
    sh_saves = models.IntegerField(blank=True, null=True)
    even_saves = models.IntegerField(blank=True, null=True)
    sh_shots = models.IntegerField(blank=True, null=True)
    even_shots = models.IntegerField(blank=True, null=True)
    pp_shots = models.IntegerField(blank=True, null=True)
    sv_pct = models.FloatField(blank=True, null=True)
    gaa = models.FloatField(blank=True, null=True)
    games = models.IntegerField(blank=True, null=True)
    games_started = models.IntegerField(blank=True, null=True)
    shots_against = models.IntegerField(blank=True, null=True)
    goals_against = models.IntegerField(blank=True, null=True)
    toi_per_game = models.CharField(max_length=20, blank=True, null=True)
    pp_sv_pct = models.FloatField(blank=True, null=True)
    sh_sv_pct = models.FloatField(blank=True, null=True)
    ev_sv_pct = models.FloatField(blank=True, null=True)

    def __str__(self):
        return (
            f"{self.player.full_name}, {self.player.current_team.name}, {self.season}"
        )
