from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.index),
    url(r'^dang-nhap.html$', views.login),
    url(r'^404.html$', views.notfound),
    url(r'^dang-xuat.html$', views.logout),
]

