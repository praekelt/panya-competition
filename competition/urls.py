from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    'competition.views',
    url(r'^list/$', 'object_list', name='competition_object_list'),
    url(r'^(?P<slug>[\w-]+)/$', 'object_detail', name='competition_object_detail'),
)
