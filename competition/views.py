from panya.generic.views import GenericObjectList, GenericObjectDetail
from competition.models import Competition, CompetitionPreferences
from competition.pagemenus import CompetitionPageMenu

class ObjectList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        extra_context = super(ObjectList, self).get_extra_context(*args, **kwargs)
        added_context = {'title': 'Competitions'}
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context
    
    def get_pagemenu(self, request, queryset, *args, **kwargs):
        return CompetitionPageMenu(queryset=queryset, request=request, slug=None)

    def get_paginate_by(self):
        return 7
    
    def get_queryset(self):
        return Competition.permitted.all().order_by('start_date')

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_extra_context(self, slug, *args, **kwargs):
        extra_context = super(ObjectDetail, self).get_extra_context(*args, **kwargs)
        added_context = {
            'title': 'Competitions',
        }
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context
    
    def get_pagemenu(self, request, queryset, slug, *args, **kwargs):
        return CompetitionPageMenu(queryset=queryset, request=request, slug=slug)

    def get_queryset(self, slug):
        return Competition.permitted.all()
        
object_detail = ObjectDetail()

class OptionDetail(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        extra_context = super(OptionDetail, self).get_extra_context(*args, **kwargs)
        added_context = {'title': 'Competitions'}
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context
    
    def get_pagemenu(self, request, queryset, *args, **kwargs):
        return CompetitionPageMenu(queryset=queryset, request=request, slug=None)

    def get_paginate_by(self):
        return 1
    
    def get_queryset(self):
        return CompetitionPreferences.objects.all()

    def get_template_name(self):
        return 'competition/competitionoptions_list.html'
        
option_detail = OptionDetail()
