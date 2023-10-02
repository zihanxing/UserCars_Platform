
from django.shortcuts import render, redirect

def redirectindex(request):  # 重定向主页
    return redirect("/myblog/index")

def error404(request):
    return render(request, "404error.html", {"index": 99})