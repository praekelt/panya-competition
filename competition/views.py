from content.filters import IntervalOrderFilterSet
from content.generic.views import GenericObjectDetail, GenericObjectList 
from competition.models import Competition

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
    
    def get_filterset(self, request, queryset):
        return IntervalOrderFilterSet(request.GET, queryset=queryset)
    
    def get_paginate_by(self):
        return 12
    
    def get_queryset(self):
        return Competition.permitted.all()

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_queryset(self):
        return Competition.permitted.all()
    
    def get_extra_context(self):
        return {'title': 'Competitions'}

object_detail = ObjectDetail()
