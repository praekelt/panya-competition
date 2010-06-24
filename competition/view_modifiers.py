from panya.view_modifiers import ViewModifier
from panya.view_modifiers.items import URLPatternItem
from django.core.urlresolvers import reverse

class CompetitionViewModifier(ViewModifier):
    def __init__(self, request, *args, **kwargs):
        self.items = [
            URLPatternItem(request, title="Current Competitions", path=reverse('competition_object_list', kwargs={}), matching_pattern_names=['competition_object_list',], default=False),
            URLPatternItem(request, title="Competition Rules", path=reverse('competition_preferences_detail', kwargs={}), matching_pattern_names=['competition_preferences_detail',], default=False),
        ]
        super(CompetitionViewModifier, self).__init__(request, *args, **kwargs)
