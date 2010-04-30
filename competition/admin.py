from django.contrib import admin

from content.admin import ModelBaseAdmin
from competition.models import Competition, CompetitionEntry

    
admin.site.register(Competition, ModelBaseAdmin)
admin.site.register(CompetitionEntry)
