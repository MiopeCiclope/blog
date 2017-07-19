from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'', include('blog.urls', namespace='blog')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'accounts/', include('accounts.urls', namespace='accounts')),
    url('^markdown/', include( 'django_markdown.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)