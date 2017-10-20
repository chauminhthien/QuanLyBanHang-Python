from django.shortcuts import render
from django.http import HttpResponse
from Home.models import *
from django.contrib import messages
import hashlib
from django.shortcuts import redirect
import datetime
from time import time
import os

def danhSachCate(request):
	Data = {
		'user': request.session['keyUser'],
		'cates' : Cate.objects.all()
	}
	return render(request, 'site/cate/danhsach.html', Data)

def themCate(request):
	Data = {
		'user': request.session['keyUser']
	}
	if request.method == "POST":
		theloai = request.POST['theloai']
		Cate(name = theloai).save()
		messages.success(request, "Thêm Thể Loại Thành Công")
		return redirect('/the-loai/them-cate.html')
	return render(request, 'site/cate/them.html', Data)

def suaCate(request, id):
	Data = {
		'user': request.session['keyUser'],
		'cate': Cate.objects.get(id = id)
	}
	if request.method == "POST":
		theloai = request.POST['theloai']
		cate = Cate.objects.get(id = id)
		cate.name = theloai
		cate.save()
		messages.success(request, "Sửa Thể Loại Thành Công")
		return redirect('/the-loai/sua-the-loai/'+id)
	return render(request, 'site/cate/sua.html', Data)

def xoaCate(request, id):
	pro = Product.objects(idCate = id).count()
	if(pro > 0):
		messages.error(request, "Không thể Xoá Thể loại Này! Vui Lòng Xem lại !!!")
	else:
		Cate.objects.get(id = id).delete()
		messages.success(request, "Đã Xoá Thành Công")
	return redirect('/the-loai/danh-sach.html')
