from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'(?P<id>\d+)/$', views.details, name='details'),
    url(r'(?P<id>\d+)/vote/$', views.vote, name='vote'),
    url(r'(?P<id>\d+)/results/$', views.results, name='results'),
)
