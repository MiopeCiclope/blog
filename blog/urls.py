from django.conf.urls import include, url
from . import views
from blog.views import PostListView

app_name='blog'

urlpatterns = [
    url(r'^(?P<category>[a-zA-Z0-9-]*)$', PostListView.as_view(), name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^asdf/$', views.tst),
    url(r'^googlef6613f69040c50ea.html$', views.google),
    url(r'^like_category/$', views.like_category, name='like_category'),
]