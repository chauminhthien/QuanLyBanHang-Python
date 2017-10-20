from mongoengine import *

class User(Document):
    email = StringField()
    password = StringField()
    img = StringField()
    fullname = StringField()
    token = StringField()

class Cate(Document):
    name = StringField()

class Product(Document):
    name = StringField()
    soluong = StringField()
    idCate = StringField()
    hinh = StringField()
    gia = StringField()

class Bill(Document):
    name = StringField()
    sdt = StringField()
    diachi = StringField()
    sanpham = StringField()
    time = StringField()

class Test(Document):
    name = StringField()
    email = StringField()




