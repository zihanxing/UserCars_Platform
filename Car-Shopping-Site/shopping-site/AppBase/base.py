from django.shortcuts import render, redirect
from AppBase.models import UserDict
from django.db.models import Q
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime, time
import copy
import json
import os
import sys
from django.conf import settings
import subprocess
from django.db.models import Q
from django.db.models import F
from django.core.paginator import Paginator
from django.views import View

#判断用户是否登陆
def checkLogin(func):
    def wrapper(request, *args, **kwargs):
        # if request.session.get('username', False):
        #     #校验用户合法
        #     currentUser = getCurrentUser(request.session.get('username'))
        #     if currentUser== "":
        #         return redirect("/myblog/error?ErrorMessage=" + "用户已不存在")
        #     return func(request, *args, **kwargs)
        # else:
        #     return  redirect("/login")
        if request.user.is_anonymous:
        #if not request.user.authenticated():
            return redirect('/login')
        else:
            return func(request, *args, **kwargs)
    return wrapper


#根据username 返回 user
def getCurrentUser(username):
    users = UserDict.objects.filter(Q(name=username) | Q(email=username) | Q(phone=username))
    if len(users) <= 0:
        return ""
    else:
        return users[0]

#根据request 返回 user
def getRequestUser(request):
    username = request.session.get('username', '')
    users = UserDict.objects.filter(Q(name=username) | Q(email=username) | Q(phone=username))
    if len(users) <= 0:
        return ""
    else:
        return users[0]


def successResponseCommon(data, message="success"):
    return HttpResponse(json.dumps({"code": 200, "data": data, "message": message}, ensure_ascii=False), content_type="application/json")

def errorResponseCommon(data, message):
    return HttpResponse(json.dumps({"code": 500, "data": data, "message": message}, ensure_ascii=False), content_type="application/json")

def failedResponseCommon(code,data, message="failed"):
    return HttpResponse(json.dumps({"code": code, "data": data, "message": message}, ensure_ascii=False), content_type="application/json")



def timeConverStr(timepar):
    #timepar=datetime.strptime(timepar, '%Y-%m-%d %H:%M:%S') #字符串转时间
    return timepar.strftime('%Y-%m-%d %H:%M:%S')