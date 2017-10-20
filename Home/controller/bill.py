from django.shortcuts import render
from django.http import HttpResponse
from Home.models import *
from django.shortcuts import redirect
import os
from time import time
from django.contrib import messages
import re
import json

def lapBill(request):
    if('keyOrder' in request.session):
        del request.session['keyOrder']
    Data = {
		'user': request.session['keyUser']
	}

    if request.method=='POST':
        print(request.session['keyOrder'])
        
    return render(request, 'site/bill/newBill.html', Data)

def ajaxGetOrder(request):
    txt = ""
    if request.is_ajax():
        if request.method=='POST':
            name    = request.POST['name']
            soluong = request.POST['soluong']
            regex = re.compile('.*'+name+'.*')
            products = Product.objects(name = regex)
            for product in products:
                txt += '<div class="item" st="'+ str(product.id)+'">'
                txt+= '<div class="col-md-3">'
                txt+= '<img src="/static/upload/product/'+product.hinh+'" alt="'+product.name+'" class="img-responsive">'
                txt+= '</div>'
                txt+= '<div class="col-md-9">'
                txt+= '<h5>'+product.name+' Giá: '+product.gia+' đ</h5>'
                if(int(product.soluong) < int(soluong)):
                    txt+= '<p>Không đủ hàng: chỉ còn: '+product.soluong+' sản phẩm</p>'
                txt+= '</div>'
                txt+= '<div class="cls"></div>'
                txt+= '</div>'
            
    return HttpResponse(txt)

def ajaxLapBill(request):
    data = {
        "st"    : "0",
        "mess"  : ""
    }
    if request.is_ajax():
        if request.method=='POST':
            soluong     = request.POST['soluong']
            idSp        = request.POST['id']
            product     = Product.objects.get(id = idSp)
            if('keyOrder' in request.session):
                if(idSp in request.session['keyOrder']):
                    sl = int(soluong) + int(request.session['keyOrder'][idSp][1])
                    if (int(product.soluong) < int(sl)):
                        data['mess'] = "Số Lượng Không Đủ"
                    else:
                        request.session['keyOrder'][idSp][1] = sl
                        request.session.save()
                        data['st'] = 1
                        data['mess'] = "Cập Nhật Thành Công"
                else:
                    if (int(product.soluong) < int(soluong)):
                        data['mess'] = "Số Lượng Không Đủ"
                    else:
                        bill = [
                            idSp,
                            soluong
                        ]
                        request.session['keyOrder'][idSp] = bill
                        request.session.save()
                        data['st'] = 1
                        data['mess'] = "Cập Nhật Thành Công"
            else:
                if (int(product.soluong) < int(soluong)):
                    data['mess'] = "Số Lượng Không Đủ"
                else:
                    request.session['keyOrder'] = {}

                    bill = [
                        idSp,
                        soluong
                    ]
                    request.session['keyOrder'][idSp] = bill
                    print(request.session['keyOrder'])
                    data['st'] = 1
                    data['mess'] = "Cập Nhật Thành Công"

    return HttpResponse(json.dumps(data))

def getSession(request):
    txt = '<ul class="todo-list ui-sortable">'
    tong = 0
    if request.is_ajax():
        if request.method=='POST':
            if('keyOrder' in request.session):
                sess = request.session['keyOrder']
                for item in sess:
                    product = Product.objects.get(id = item)
                    tong += int(sess[item][1]) * int(product.gia)
                    txt += '<li>'
                    txt += '<span class="handle ui-sortable-handle">'
                    txt += '<i class="fa fa-ellipsis-v"></i>'
                    txt += '<i class="fa fa-ellipsis-v"></i>'
                    txt += '</span>'
                    txt += '<span class="text">'+product.name+'</span>'
                    txt += '<small class="label label-success"><i class="fa fa-clock-o"></i> x'+str(sess[item][1])+'</small>'
                    txt += '<div class="tools">'
                    txt += '<i class="delSession fa fa-trash-o" st="'+item+'" ></i>'
                    txt += '</div>'
                    txt += '</li>'
    txt += '</ul>'
    txt += '<h2><strong>Tổng:</strong>  <span id="tiền">'+str(tong)+'đ</span></h2>'

    return HttpResponse(txt)


def ajaxDelBill(request):
    data = {
        "st"    : "0",
        "mess"  : "Có lổi Xảy ra"
    }
    if request.is_ajax():
        if request.method=='POST':
            idSp        = request.POST['id']
            if(idSp in request.session['keyOrder']):     
                del request.session['keyOrder'][idSp]
                request.session.save()
                data['st'] = 1
                data['mess'] = "Xoá Sản phẩm thành công"

    return HttpResponse(json.dumps(data))

def dathangsession(request):
    if request.method=='POST':
        if('keyOrder' in request.session):
            sess = request.session['keyOrder']
            if(len(sess) > 0):
                sp = ""
                for item in sess:
                    product = Product.objects.get(id = item)
                    sp += item + "-" + str(sess[item][1]) + ";"
                    product.soluong = str(int(product.soluong) - int(sess[item][1]))
                    product.save()
                sp = sp[0:(len(sp) -1)]
                bill = Bill()
                bill.name = request.POST['name']
                bill.sdt = request.POST['sdt']
                bill.diachi = request.POST['diachi']
                bill.sanpham = sp
                bill.time = repr(time())
                bill.save()

                messages.success(request, 'Đặt hàng Thành Công')
                return redirect('/bill/lap-don-hang-new.html')
            else:
                messages.error(request, 'Chưa chọn sản phẩm đặt hàng')
                return redirect('/bill/lap-don-hang-new.html')
        else:
            messages.error(request, 'Chưa chọn sản phẩm đặt hàng')
            return redirect('/bill/lap-don-hang-new.html')

           
    return HttpResponse("ok")