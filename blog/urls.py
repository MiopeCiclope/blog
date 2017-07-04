from django.conf.urls import include, url
from . import views
from blog.views import PostListView

urlpatterns = [
    url(r'^$', PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
]