# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from login.models import VIP
import re


# Create your views here.
def index(request):
    return render(request, "index.html")
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        namepattern = re.match(r"1\d{10}", username)
        password = request.POST.get('password', '')
        pwpattern = re.match(r"[\w]{6,12}", password)
        if namepattern:
            try:
                vipuser = VIP.objects.get(name=username)
                if vipuser is not None:
                    if vipuser.password == password:
                        user = auth.authenticate(username=username,password=password)
                        auth.login(request, user)
                        request.session['user'] = username
                        return render(request,'success.html',{'user':username})
                        #response = HttpResponseRedirect('/success/')
                       # return response
                    else:
                        return render(request, "index.html", {'error': ' 密码或者用户名错误!'})
            except VIP.DoesNotExist:
                    return render(request, "index.html", {'error': '该用户尚未注册!'})
        return render(request, "index.html", {'error': '请输入正确的手机号!'})
    return render(request, "index.html")

def success(request):
    username = request.session.get('user', '')
    return render(request, 'success.html', {'user': username})
def register(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        namepattern=re.match(r"1\d{10}", username)
        password = request.POST.get('password', '')
        pwpattern = re.match(r"^[\w]{6,12}$",password)
        if namepattern:
            try:
                user = VIP.objects.get(name=username)
                if user is not None:
                    return render(request,'register.html',{'error':'该用户已经注册过了'})
            except VIP.DoesNotExist:
                if pwpattern:
                    VIP.objects.create(name=username,password=password)
                    return render(request,"success2.html")
                else:
                    return render(request,'register.html',{'error': '请输入6-12位密码，只能是字母、数字和下划线'})
        else:
            return render(request,"register.html",{'error': '请输入11位合法的手机号!'})

    return render(request,'register.html')



