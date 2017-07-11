from django.conf.urls import include, url
from . import views
from blog.views import PostListView, PostListViewGarbage, PostListViewLoved, PostListViewDrunk

app_name='blog'

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^garbage/$', PostListViewGarbage.as_view(), name='garbage_list'),
    url(r'^loved/$', PostListViewLoved.as_view(), name='loved_list'),
    url(r'^drunk/$', PostListViewDrunk.as_view(), name='drunk_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^asdf/$', views.tst),
    url(r'^googlef6613f69040c50ea.html$', views.google),
]