from django.urls import path, re_path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('', views.home, name='PicCode-home'),
    path('decode/', views.decode, name='PicCode-decode'),
    path('encode/', views.encode, name='PicCode-encode'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += re_path(r'^media/(?P<path>.*)$',serve,{'document_root':settings.MEDIA_ROOT})