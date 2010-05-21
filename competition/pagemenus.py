from pagemenu.pagemenus import PageMenu
from pagemenu.items import URLPatternItem
from django.core.urlresolvers import reverse

class CompetitionPageMenu(PageMenu):
    def __init__(self, queryset, request, slug, *args, **kwargs):
        self.items = [
            URLPatternItem(request, title="Current Competitions", path=reverse('competition_object_list', kwargs={}), matching_pattern_names=['competition_object_list', 'competition_object_detail',], default=False),
            URLPatternItem(request, title="Competition Rules", path=reverse('competition_option_detail', kwargs={}), matching_pattern_names=['competition_option_detail',], default=False),
        ]
        super(CompetitionPageMenu, self).__init__(queryset, request)
