from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stu_list, name='stu_list'),
    url(r'^new/$', views.new_stu, name='new_stu'),
    url(r'^update/(?P<pk>\d+)$', views.update_stu, name='update_stu'),
    url(r'^delete/(?P<pk>\d+)$', views.delete_stu, name='delete_stu'),
    url(r'^detail/(?P<pk>\d+)$', views.detail_stu, name='detail_stu'),
    # url(r'^(?P<pk>\d+)/$', views.student_detail, name='student_detail'),
    # url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]