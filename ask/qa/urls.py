from django.conf.urls import patterns, include, url
from qa.views import show, test

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('qa.views',
    url(r'^aaa/', include(admin.site.urls)),
    url(r'^login/', 'test', name='login'),
    url(r'^signup/', 'test', name='signup'),
    url(r'^question/(?P<id>\d+)/', 'test', name='id'),
    url(r'^ask/', test, name='ask'),
    url(r'^popular/', show, name='popular'),
    url(r'^new/', test, name='new'),   
    url(r'^', show, name='all'),
)
