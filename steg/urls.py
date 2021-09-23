from django.urls import path
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='PicCode-home'),
    path('decode/', views.decode, name='PicCode-decode'),
    path('encode/', views.encode, name='PicCode-encode'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)