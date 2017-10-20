from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from .models import *
from django.shortcuts import render

class ApplowMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request = self.get_response(request)
        return request
    #def process_request():

    def process_exception(self, request, exception):
        return redirect('/404.html')

    #def process_request(self, request):
    #    request.session['aaaa'] = 'aaaaaaaaaaa'
    #    print(request)
    #    return None
    #def process_response(self, request):
    #    request.session['aaaa'] = 'aaaaaaaaaaa'
    #    print(request)
    #    return None
    #def process_template_response(self, request):
    #    print("aaaaaaaaa")
    #    return None

    def error_404(request):
        data = {}
        return render(request,'myapp/error_404.html', data)

    def process_view( self, request, view_func, view_args, view_kwargs ):
        #print(request.session['aaaaaaaaaa'])
        #request.session['keyUser'] = 'aaaaaaaaaaa'
        path = request.path_info.lstrip('/')
        if (path == "dang-nhap.html" or path == "404.html"):
            next
        else:
            if ('keyUser' in request.session):
                user = User.objects.get(email = request.session['keyUser']['email'], password = request.session['keyUser']['password'])
                if(request.session['keyUser']['token'] == user.token):
                    next
                else:
                    messages.error(request, "Có Người đã đăng nhập tài khoảng này!!")
                    return redirect('/dang-nhap.html')
            else:
                return redirect('/dang-nhap.html')