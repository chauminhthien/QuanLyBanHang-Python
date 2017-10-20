from django.conf.urls import url
from Home.controller import product
urlpatterns = [
    url(r'^danh-sach.html', product.danhSachProduct),
    url(r'^them-san-pham.html', product.themProduct),
    url(r'^sua-san-pham/(?P<id>\w+)', product.suaProduct),
    url(r'^xoa/(?P<id>\w+)', product.delProduct),
]