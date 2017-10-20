from django.conf.urls import url
from Home.controller import thongke
urlpatterns = [
    url(r'^san-pham-het-hang.html', thongke.danhsachHetHang),
    url(r'^export-san-pham-het-hang.html', thongke.exportHetHang),
    url(r'^don-hang.html', thongke.getDonHang),
    url(r'^view/(?P<id>\w+)', thongke.getViewDonHang),
    url(r'^export-don-hang.html', thongke.exportDonHang),
]