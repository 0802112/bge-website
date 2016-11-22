from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stu_list, name='stu_list'),
    url(r'^new/$', views.new_stu, name='new_stu'),
]