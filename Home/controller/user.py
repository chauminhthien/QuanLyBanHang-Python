from django.shortcuts import render
from django.http import HttpResponse
from Home.models import *
from django.shortcuts import redirect
import os
from django.contrib import messages
import hashlib
from time import time

def profileUser(request):
	Data = {
		'user': request.session['keyUser']
	}
	user = User.objects.get(id = request.session['keyUser']['id'])

	if request.method == "POST":
		user.fullname = request.POST['fullname']
		if(request.POST['password']  != ""):
			password = request.POST['password']
			password = hashlib.md5(password.encode('utf-8')).hexdigest()
			user.password = password
		user.save()
		messages.success(request, "Cập Nhập Thông Tin Thành Công !! Vui Lòng đăng Nhập lại")
		return redirect('/dang-nhap.html')

	return render(request, 'site/user/profile.html', Data)

def userUpload(request):
	if request.method == 'POST':
		fileU = request.FILES['avatar']
		t = repr(time()) + "_"
		fileU.name = t + fileU.name

		upload(fileU)
		user = User.objects.get(id = request.session['keyUser']['id'])
		try:
			os.remove('Home/static/upload/user/'+  user.img)
		except:
			print("aaaaaaa")
		user.img = fileU.name
		user.save()
		messages.success(request, "Cập Nhập Thông Tin Thành Công !! Vui Lòng đăng Nhập lại")
		return redirect('/dang-nhap.html')
def upload(f):
    with open('Home/static/upload/user/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)