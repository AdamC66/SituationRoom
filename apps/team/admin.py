from django.contrib import admin

# Register your models here.
from apps.team.models import Team, TeamRecords

admin.site.register(Team)
admin.site.register(TeamRecords)
