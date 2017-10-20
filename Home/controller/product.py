from django.shortcuts import render
from django.http import HttpResponse
from Home.models import *
from django.shortcuts import redirect
import os
from time import time
from django.contrib import messages

def danhSachProduct(request):
	
	products = Product.objects().all()
	pro = []
	for product in products:
		cate = Cate.objects.get(id = product.idCate)
		product.theloai = cate.name
		pro.append(product)
			
	Data = {
		'user': request.session['keyUser'],
		'products': pro
	}
	return render(request, 'site/product/danhsach.html', Data)

def themProduct(request):
	Data = {
		'user': request.session['keyUser'],
		'cates': Cate.objects().all()
	}
	if request.method == 'POST':
		fileU = request.FILES['hinhanh']
		t = repr(time()) + "_"
		fileU.name = t + fileU.name
		upload(fileU)

		product 			= Product()
		product.name 		= request.POST['sanpham']
		product.soluong 	= request.POST['soluong']
		product.idCate 		= request.POST['theloai']
		product.hinh 		= fileU.name
		product.gia 		= request.POST['gia']
		product.save()
		messages.success(request, "Thêm Sản Phẩm Thành Công")
		return redirect('/san-pham/them-san-pham.html')
	return render(request, 'site/product/them.html', Data)


def suaProduct(request, id):
	Data = {
		'user'		: request.session['keyUser'],
		'cates'		: Cate.objects().all(),
		'products' 	: Product.objects.get(id = id)
	}
	if request.method == 'POST':
		product = Product.objects.get(id = id)
		product.name 		= request.POST['sanpham']
		product.soluong 	= request.POST['soluong']
		product.idCate 		= request.POST['theloai']
		product.gia 		= request.POST['gia']

		if (request.FILES):
			fileU = request.FILES['hinhanh']
			t = repr(time()) + "_"
			fileU.name = t + fileU.name
			upload(fileU)
			try:
				os.remove('Home/static/upload/product/'+ product.hinh)
			except:
				print("error")

			product.hinh 		= fileU.name
		product.save()
		messages.success(request, "Cập Nhật Sản Phẩm Thành Công")
		return redirect('/san-pham/sua-san-pham/'+id)

	return render(request, 'site/product/sua.html', Data)

def delProduct(request, id):
	product = Product.objects.get(id = id)
	try:
		os.remove('Home/static/upload/product/'+ product.hinh)
	except:
		print("error")
	product.delete()
	messages.success(request, "Xoá Sản Phẩm Thành Công")
	return redirect('/san-pham/danh-sach.html')

def upload(f):
    with open('Home/static/upload/product/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)