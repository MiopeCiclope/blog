from django.conf.urls import include, url
from django.contrib.auth.views import login, logout, password_change, password_change_done

urlpatterns = [
    url(
        r'login/$',
        login,
        name='login',
        kwargs={'template_name': 'login.html'}
    ),
    url(
        r'^logout/$',
        logout,
        name='logout',
        kwargs={'next_page': '/'}
    ),
    
    url(
        r'^password_change$',
        password_change,
        name='password_change',
        kwargs={
               'template_name': 'password_change_form.html',
               'post_change_redirect':'accounts:password_change_done',
               }
    ),
    url(
        r'^password_change_done$',
        password_change_done,
        name='password_change_done',
        kwargs={'template_name': 'password_change_done.html'}
    ),
]