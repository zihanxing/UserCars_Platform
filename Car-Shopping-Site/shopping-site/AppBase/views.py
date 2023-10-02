from AppBase.base import  *
from django.utils.decorators import method_decorator
from django.contrib.auth import authenticate, login,logout
import  random
from AppBase.sendEmail import *
# Create your views here.

# 主页
@method_decorator(checkLogin, name='dispatch')
class IndexView(View):
    def get(self, request):
        print('request.user', request.user.username)
        print('request.user', request.user.id)
        # 下面是判断是是否是匿名
        print('request.user', request.user.is_anonymous)
        username = request.user.username
        return render(request, "error.html",
                      {"code": 200, "message": username})


#登录
class LoginView(View):
    def get(self,request):
        return render(request, "login.html", {"index": 99})
    def post(self,request):
        username = request.POST.get('username',"")
        # 判断用户名 密码是否合法用户
        password = request.POST.get('password',"")
        # 进行数据校验
        if not all([username, password]):
            return render(request, "error.html",{"code":500,"message":"用户名或密码未输入"})
        #根据输入username(可以是邮箱 手机号码 用户名 三者都是唯一值)查询username
        try:
            user = models.UserDict.objects.get(Q(phone=username) | Q(email=username) | Q(username=username))
        except models.UserDict.DoesNotExist:  # 可以捕获除与程序退出sys.exit()相关之外的所有异常
            return render(request, "error.html",{"code":500,"message":"用户不存在"})
        #验证密码
        user = authenticate(username=user.username, password=password)  # 用户验证
        if user:
            login(request, user)  # 用户登录
            request.session['username'] = username
            return redirect('/index')
        return render(request, "error.html",{"code":500,"message":"密码错误"})

#注销
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect("/login")


#注册
class RegistView(View):
    def post(self,request):
        username = request.POST.get('username',"")
        # useremail = request.POST.get('email')
        password = request.POST.get('password')
        role= request.POST.get('role')
        # if username=="":
        #     username=useremail
        if not all([username, password]):
            return render(request, "error.html",{"code":500,"message":"用户名或密码未输入"})
        # 判断名字是否已存在
        users = models.UserDict.objects.filter(Q(username=username))
        if len(users) <= 0:
            user=models.UserDict.objects.create_user(username=username, email=username, phone=username, password=password,role=role)
            login(request, user)  # 用户登录
            return redirect("/index")
        else:
            return render(request, "error.html",{"code":500,"message":"用户名已被注册"})


class RegistAPIView(View):
    def post(self,request):
        username = request.POST.get('name',"")
        # useremail = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role')
        # if username=="":
        #     username=useremail
        if not all([password]):
            return errorResponseCommon({},"Please fill the password")
        # 判断名字是否已存在
        users = models.UserDict.objects.filter(Q(username=username))
        if len(users) <= 0:
            # # 邮箱验证发送邮件
            # res = SendEmail(useremail, "感谢注册电商", "网站后续完善中，后续更多精彩，敬请期待！")
            # if res == "success":
                # 随机头像
                iocnList = models.AppDefaultIocn.objects.all()
                if len(iocnList) > 0:
                    iocnIndex = random.randint(0, len(iocnList)-1)
                    user = models.UserDict.objects.create_user(username=username, email=username, phone="",role=role,
                                                               password=password, img=iocnList[iocnIndex].img)
                else:
                    user = models.UserDict.objects.create_user(username=username, email=username, phone="",role=role,
                                                               password=password)
                login(request, user)  # 用户登录
                return successResponseCommon({"url": "/shop/index"}, "注册成功")
            # else:
            #     return errorResponseCommon({}, "邮箱验证失败！")



        else:
            #精确提示什么已被注册
            if len(models.UserDict.objects.filter(Q(username=username)))>0:
                return errorResponseCommon({}, "用户名已被注册")
            return errorResponseCommon({},"邮箱已被注册")

class LoginAPIView(View):
    def post(self,request):
        username = request.POST.get('username',"")
        # 判断用户名 密码是否合法用户
        password = request.POST.get('password',"")
        # 进行数据校验
        if not all([username, password]):
            return errorResponseCommon({},"用户名或密码未输入")
        #根据输入username(可以是邮箱 手机号码 用户名 三者都是唯一值)查询username
        try:
            user = models.UserDict.objects.get(Q(phone=username) | Q(email=username) | Q(username=username))
        except models.UserDict.DoesNotExist:  # 可以捕获除与程序退出sys.exit()相关之外的所有异常
            return errorResponseCommon({},"用户不存在")
        #验证密码
        user = authenticate(username=user.username, password=password)  # 用户验证
        if user:
            login(request, user)  # 用户登录
            request.session['username'] = username
            return successResponseCommon({"url":"/index"},"登录成功")
        return errorResponseCommon({},"密码错误")



class ProfileView(View):
    def get(self, request):
        return render(request, "VersionApp/profile.html", {"index": 99})


@method_decorator(checkLogin, name='dispatch')
class UserInfoView(View):
    def get(self, request):
        id = request.GET.get("id", 0)
        if id==0:
            id=request.user.id
        return render(request, "ShoppingApp/user_info.html", {"id": id})

class UserInfoDataView(View):
    def get(self, request):
        id = request.GET.get("id", 0)
        user=UserDict.objects.get(id=id)
        data={"id":user.id,"username":user.username,"email":user.email,"phone":user.phone,"img":user.img.url}
        return successResponseCommon(
            {"items": data, "pages": 1, "curpage": 1,
             "sumNum": 1,
             "nodataflag": 1})
    def post(self,request):
        #修改用户信息
        data = request.POST
        id = data.get('id', 0)
        username = data.get("username", "")
        email = data.get("email", "")
        phone = data.get("phone", "")
        psd = data.get("psd", "")
        dataitem = models.UserDict.objects.get(id=id)
        dataitem.username = username
        if psd != "123456":
            dataitem.set_password(psd)
        dataitem.email = email
        dataitem.phone = phone
        if request.FILES:
            pic = request.FILES.get('pic')
            dataitem.img = pic
        dataitem.save()
        return successResponseCommon({}, "修改成功！")
