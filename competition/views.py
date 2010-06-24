from competition.models import Competition, CompetitionPreferences
from competition.view_modifiers import CompetitionViewModifier
from panya.generic.views import GenericObjectList, GenericObjectDetail
from preferences import preferences

class ObjectList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Competitions'}
   
    def get_view_modifier(self, request, *args, **kwargs):
        return CompetitionViewModifier(request=request, slug=None)
    
    def get_paginate_by(self, *args, **kwargs):
        return 7
    
    def get_queryset(self, *args, **kwargs):
        return Competition.permitted.all().order_by('start_date')

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Competitions'}
    
    def get_view_modifier(self, request, *args, **kwargs):
        return CompetitionViewModifier(request=request, slug=None)
    
    def get_queryset(self, *args, **kwargs):
        return Competition.permitted.all()
        
object_detail = ObjectDetail()

class PreferencesDetail(GenericObjectDetail):
    def get_extra_context(self, *args, **kwargs):
        return {'title': 'Competitions'}
    
    def get_view_modifier(self, request, *args, **kwargs):
        return CompetitionViewModifier(request=request, slug=None)
    
    def get_queryset(self, *args, **kwargs):
        return CompetitionPreferences.objects.all()

    def get_template_name(self, *args, **kwargs):
        return 'competition/competitionpreferences_detail.html'
    
    def __call__(self, request, *args, **kwargs):
        self.params['object_id'] = preferences.CompetitionPreferences.id
        return super(PreferencesDetail, self).__call__(request, *args, **kwargs)
        
preferences_detail = PreferencesDetail()
