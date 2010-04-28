from django.contrib import admin

from content.admin import ModelBaseAdmin
from competition.models import Competition, CompetitionOption, CompetitionEntry


class CompetitionOptionInline(admin.TabularInline):
    model = CompetitionOption
    fk_name = 'competition'
    extra = 1

class CompetitionEntryInline(admin.TabularInline):
    model = CompetitionEntry
    fk_name = 'competition'
    extra = 1
    
class CompetitionAdmin(ModelBaseAdmin):
    inlines = (
        CompetitionOptionInline,
        CompetitionEntryInline
    )
    
admin.site.register(Competition, CompetitionAdmin)
