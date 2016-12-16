from django.conf.urls import url
from potential_stu.views import stu_list, new_stu, update_stu, delete_stu, detail_stu

urlpatterns = [
    url(r'^$', stu_list, name='potential_stu_list'),
    url(r'^new/$', new_stu, name='new_potential_stu'),
    url(r'^update/(?P<pk>\d+)$', update_stu, name='update_potential_stu'),
    url(r'^delete/(?P<pk>\d+)$', delete_stu, name='delete_potential_stu'),
    url(r'^detail/(?P<pk>\d+)$', detail_stu, name='detail_potential_stu'),
]