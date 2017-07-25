"""nscheoausc URL Configuration"""


from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import LoginView
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^login/$', LoginView.as_view(), name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),

    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('users.urls', namespace='users')),
    url(r'^info/', include('posts.urls', namespace='posts')),
]


if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
