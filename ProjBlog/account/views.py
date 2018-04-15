from django.shortcuts import render,HttpResponse

# Create your views here.

from account.forms import LoginForm,RegistrationForm,UserProfileForm
from django.contrib.auth import authenticate,login

def user_login(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request,'account/login.html',{'form':form})

    if request.method == "POST":
        lf = LoginForm(request.POST)
        if lf.is_valid():
            cd = lf.cleaned_data
            user = authenticate(**cd)   # 确认该用户在数据库中是否存在
            if user:
                login(request,user)
                return HttpResponse("欢迎用户%s登录" % cd['username'])
            else:
                return HttpResponse('您输入的用户名或者密码不对')
        else:
            return HttpResponse('登录无效')

def register(request):
    if request.method == "POST":
        print(request.POST)
        user_form = RegistrationForm(request.POST)
        user_form.as_p()
        userprofile_form = UserProfileForm(request.POST)
        if user_form.is_valid() and userprofile_form.is_valid():
            new_user = user_form.save(commit=False)    # new_user : 就是存入的那条记录
            new_user.set_password(user_form.cleaned_data['password'])   # p64
            new_user.save()
            new_profile = userprofile_form.save(commit=False)
            print("new_profile",new_profile)
            new_profile.user = new_user
            new_profile.save()
            return HttpResponse('注册成功')
        else:
            return HttpResponse('对不起，您输入格式不对，无法注册' )
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,'account/register.html',{'form':user_form,'profile':userprofile_form})



