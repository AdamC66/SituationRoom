from django.contrib import admin
from .models import SituationRoomUser

admin.site.register(SituationRoomUser, admin.ModelAdmin)