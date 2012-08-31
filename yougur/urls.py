from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^menus/$', 'menus.views.index'),
    url(r'^menus/(?P<menu_id>\d+)/$', 'menus.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
) 