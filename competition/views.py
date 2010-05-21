from content.generic.views import GenericObjectList, GenericObjectDetail
from competition.models import Competition
from pagemenu.pagemenus import DateFieldIntervalPageMenu

class ObjectList(GenericObjectList):
    def get_extra_context(self, *args, **kwargs):
        extra_context = super(ObjectList, self).get_extra_context(*args, **kwargs)
        added_context = {'title': 'Competition'}
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context
    
    def get_pagemenu(self, request, queryset, *args, **kwargs):
        return None#DateFieldIntervalPageMenu(queryset=queryset, request=request, field_name='start')

    def get_paginate_by(self):
        return 7
    
    def get_queryset(self):
        return Competition.permitted.all().order_by('start_date')

object_list = ObjectList()

class ObjectDetail(GenericObjectDetail):
    def get_extra_context(self, slug, *args, **kwargs):
        extra_context = super(ObjectDetail, self).get_extra_context(*args, **kwargs)
        added_context = {
            'title': 'Competition',
        }
        if extra_context:
            extra_context.update(
                added_context,
            )
        else:
            extra_context = added_context

        return extra_context
    
    def get_pagemenu(self, request, queryset, *args, **kwargs):
        return None

    def get_queryset(self, slug):
        return Competition.permitted.all()
        
object_detail = ObjectDetail()
