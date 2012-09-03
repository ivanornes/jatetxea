from django.conf.urls import patterns, include, url
from django.views.generic import DetailView, ListView
from menus.models import Menu

urlpatterns = patterns('',
    url(r'^$',
        ListView.as_view(
            queryset=Menu.objects.order_by('-fecha')[:5],
            context_object_name='latest_menu_list',
            template_name='menus/index.html'),
        name='menu_index'),
    url(r'^(?P<pk>\d+)/$',
        DetailView.as_view(
            model=Menu,
            template_name='menus/detail.html'),
        name='menu_detail'),
)