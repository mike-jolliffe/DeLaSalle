from django.contrib import admin
from pages.models import Team, Player, Supporter


admin.site.register(Player)

class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('eventbrite_funds',)

admin.site.register(Team, TeamAdmin)

admin.site.register(Supporter)