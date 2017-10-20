from django.conf.urls import url
from Home.controller import user
urlpatterns = [
    url(r'^profile.html', user.profileUser),
    url(r'^upload.html', user.userUpload),
]