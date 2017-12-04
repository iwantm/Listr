from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^task/new/$', views.task_new, name='task_new'),
    url(r'^data/(?P<pk>\d+)/edit/$', views.task_edit, name='task_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
]
