from django.conf.urls import url
from host_family.views import home, new_host, detail_host, update_host, delete_host

urlpatterns = [
    url(r'^$', home, name='host_list'),
    url(r'^new/$', new_host, name='new_host'),
    url(r'^detail/(?P<pk>\d+)$', detail_host, name='detail_host'),
    url(r'^update/(?P<pk>\d+)$', update_host, name='update_host'),
    url(r'^delete/(?P<pk>\d+)$', delete_host, name='delete_host'),
]