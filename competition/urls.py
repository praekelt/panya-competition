from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'competition.views',
    url(r'^list/$', 'object_list', name='competition_object_list'),
    url(r'^info/$', 'preferences_detail', name='competition_preferences_detail'),
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='competition_object_detail'),
)
