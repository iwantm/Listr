from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^data/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^delete/(?P<pk>\d+)/$', views.delete, name='delete'),
]
