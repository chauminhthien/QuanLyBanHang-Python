from django.shortcuts import render
from django.http import HttpResponse
from Home.models import *
from django.shortcuts import redirect
import os
from time import time
from django.contrib import messages
import re
import csv

def danhsachHetHang(request):
    products = Product.objects(soluong = "0")
    pro = []
    for product in products:
        cate = Cate.objects.get(id = product.idCate)
        product.theloai = cate.name
        pro.append(product)

    Data = {
		'user': request.session['keyUser'],
		'products': pro
	}
    return render(request,"site/thongke/hethang.html", Data)

def exportHetHang(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="danh-sach-san-pham-het-hang.csv"'
    writer = csv.writer(response)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow(['STT', 'Tên Sách', 'Giá'])
    products = Product.objects(soluong = "0")
    i = 0
    for product in products:
        writer.writerow([i,product.name,product.gia])
        i = i + 1
    return response
    return HttpResponse("ok")

def getDonHang(request):
    bills = Bill.objects().all()
    donHang = []
    for bill in bills:
        dh = {
            "id"        : str(bill.id),
            "name"      : bill.name,
            "sdt"       : bill.sdt,
            "diachi"    : bill.diachi,
            "tien"      : "0"
        }
        tien = 0
        sps = bill.sanpham.split(';')
        for sp in sps:
            sp = sp.split('-')
            product = Product.objects.get(id = sp[0])
            tien += int(product.gia)*int(sp[1])
        dh["tien"] = str(tien)
        donHang.append(dh)
    Data = {
		'user': request.session['keyUser'],
		'donhangs': donHang
	}
    return render(request,"site/thongke/thongke.html", Data)

def getViewDonHang(request, id):
    donHang = []
    bill = Bill.objects.get(id = id)
    sps = bill.sanpham.split(';')
    tien = 0
    for sp in sps:
        sp = sp.split('-')
        product = Product.objects.get(id = sp[0])
        tien += int(product.gia)*int(sp[1])
        dh = {
            "soluong" : sp[1],
            "product" : product
        }
        donHang.append(dh)
    Data = {
		'user': request.session['keyUser'],
		'donHang': donHang,
        "tien" : tien
	}
    return render(request,"site/thongke/view.html", Data)

def exportDonHang(request):
    bills = Bill.objects().all()
    donHang = []
    for bill in bills:
        dh = {
            "name"      : bill.name,
            "sdt"       : bill.sdt,
            "diachi"    : bill.diachi,
            "tien"      : "0"
        }
        if(bill.name == ""):
            dh['name'] = "Khách Giảng Lai"
        if(bill.sdt == ""):
            dh['sdt'] = "Khách Giảng Lai"
        if(bill.diachi == ""):
            dh['diachi'] = "Khách Giảng Lai"
        
        tien = 0
        sps = bill.sanpham.split(';')
        for sp in sps:
            sp = sp.split('-')
            product = Product.objects.get(id = sp[0])
            tien += int(product.gia)*int(sp[1])
        dh["tien"] = str(tien)
        donHang.append(dh)

    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="danh-sach-don-hang.csv"'
    writer = csv.writer(response)
    response.write(u'\ufeff'.encode('utf8'))
    writer.writerow(['STT', 'Tên Khách Hàng', 'Địa Chỉ', 'SĐT', 'Tổng Tiền'])

    i = 0
    for dh in donHang:
        writer.writerow([i, dh['name'], dh['diachi'], dh['sdt'], dh['tien']])
        i = i + 1
    return response

    return HttpResponse("ok")