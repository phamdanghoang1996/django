# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

#Home
def index(request):
    ct={}
    return render(request,'home/base.html',ct)
#Công nghệ
def congnghe(request):
    ct={}
    return render(request,'home/congnghe/congnghe.html',ct)
#Khoa học
def khoahoc(request):
    ct={}
    return render(request,'home/khoahoc/khoahoc.html',ct)
#Thể thao
def thethao (request):
    ct={}
    return render(request,'home/thethao/thethao.html',ct)
#Pháp luật
def phapluat (request):
    ct={}
    return render(request,'home/phapluat/phapluat.html',ct)
#Game
def game (request):
    ct={}
    return render(request,'home/game/game.html',ct)
