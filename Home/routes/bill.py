from django.conf.urls import url
from Home.controller import bill
urlpatterns = [
    url(r'^lap-don-hang-new.html', bill.lapBill),
    url(r'^ajaxGetOrder', bill.ajaxGetOrder),
    url(r'^ajaxLapBill', bill.ajaxLapBill),
    url(r'^getSession', bill.getSession),
    url(r'^ajaxDelBill', bill.ajaxDelBill),
    url(r'^dathang.html', bill.dathangsession),
]