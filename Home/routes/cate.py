from django.conf.urls import url
from Home.controller import cate
urlpatterns = [
    url(r'^danh-sach.html', cate.danhSachCate),
    url(r'^them-cate.html', cate.themCate),
    url(r'^sua-the-loai/(?P<id>\w+)', cate.suaCate),
    url(r'^xoa/(?P<id>\w+)', cate.xoaCate),
]