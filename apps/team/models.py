from django.db import models

team_codes = {
    "Boston": "BOS",
    "Anaheim": "ANA",
    "Arizona": "ARI",
    "Buffalo": "BUF",
    "Carolina": "CAR",
    "Chicago": "CHI",
    "Calgary": "CGY",
    "Atlanta": "ATL",
    "Dallas": "DAL",
    "Colorado": "COL",
    "Edmonton": "EDM",
    "New Jersey": "NJD",
    "New YorkI": "NYI",
    "New YorkR": "NYR",
    "Columbus": "CBJ",
    "Florida": "FLA",
    "Minnesota": "MIN",
    "Los Angeles": "LAK",
    "Ottawa": "OTT",
    "Detroit": "DET",
    "Montreal": "MTL",
    "Philadelphia": "PHI",
    "Nashville": "NSH",
    "Pittsburgh": "PIT",
    "San Jose": "SJS",
    "St Louis": "STL",
    "Tampa Bay": "TBL",
    "Toronto": "TOR",
    "Phoenix": "PHX",
    "Arizona": "ARI",
    "Vancouver": "VAN",
    "Vegas": "VGK",
    "Washington": "WSH",
    "Winnipeg": "WPG",
    "Seattle": "SEA",
}


class Team(models.Model):
    DIV_CHOICES = (
        ("ATL", "Atlantic"),
        ("METRO", "Metropolitan"),
        ("PAC", "Pacific"),
        ("CEN", "Central"),
    )

    code = models.CharField(max_length=10, unique=True)
    city = models.CharField(max_length=50)
    city_name = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    nhl_api_id = models.IntegerField(null=True)
    division = models.CharField(max_length=50, null=True, choices=DIV_CHOICES)

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = team_codes[self.city]
        if self.city == "New YorkI" or self.city == "New YorkR":
            self.city_name = "New York"
        else:
            self.city_name = self.city
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

    @property
    def name(self):
        return f"{self.city_name} {self.team_name}"


class TeamRecords(models.Model):
    STREAK_CHOICES = (("wins", "wins"), ("losses", "losses"), ("ot", "ot"))
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_record")
    season = models.CharField(max_length=50)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ot = models.IntegerField()
    goals_against = models.IntegerField()
    goals_scored = models.IntegerField()
    points = models.IntegerField()
    games_played = models.IntegerField()
    streak_type = models.CharField(max_length=10)
    streak_length = models.IntegerField()
    wild_card_rank = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} - W:{} L:{} OT:{} - {}pts".format(
            self.team.name, self.wins, self.losses, self.ot, self.points
        )

    class Meta:
        ordering = ("-points",)
