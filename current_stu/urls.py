from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stu_list, name='current_stu_list'),
    url(r'^new/$', views.new_stu, name='new_stu'),
    url(r'^detail/(?P<pk>\d+)$', views.detail_stu, name='detail_current_stu'),
    url(r'^update/(?P<pk>\d+)$', views.update_stu, name='update_current_stu'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_stu, name='delete_current_stu'),
]