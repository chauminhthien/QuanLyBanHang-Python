from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.contrib import messages
import hashlib
from django.shortcuts import redirect
import datetime
from time import time
import os
# Create your views here.
#def __init__(*args, **kwargs):
#	request.session['aaaa'] = 'aaaaaaaaaaa'

def index(request):
	Data = {
		'user': request.session['keyUser'],
	}
	return render(request, 'site/home/index.html', Data)

def login(request):
	
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		password = hashlib.md5(password.encode('utf-8')).hexdigest()
		
		try:
			user = User.objects.get(email = email, password = password)
		except:
			messages.error(request, "Tài Khoảng Không Chính xác")
			return redirect('/dang-nhap.html')
		if(user):
			user.token = request.POST['csrfmiddlewaretoken']
			user.save()
			request.session['keyUser'] = user
			return redirect('/')
		else:
			messages.error(request, "Tài Khoảng Không Chính xác")
			return redirect('/dang-nhap.html')

	return render(request, 'site/login/login.html')
	
def logout(request):
	del request.session['keyUser']
	return redirect('/')

def notfound(request):
	return render(request, 'site/404/404.html')

def test(request):
	test = Test.objects.get(email = "1111111").delete()
	#test.name = "châu minh thien"
	#test.save()
	return HttpResponse("Yes")

def upload(f):
    with open('Home/static/upload/user/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)







