from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, "acc/index.html")

def userlogin(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        u = authenticate(username=un, password=up)
        if u:
            login(request, u)
            messages.success(request, f'{u}님 안녕하세요.')
            return redirect("acc:index")
        else:
            messages.error(request, '계정정보가 일치하지 않습니다.')
    return render(request, "acc/login.html")

def userlogout(request):
    logout(request)
    return redirect("acc:index")

def profile(request):
    return render(request, "acc/profile.html")

def delete(request):
    u = request.user
    cp = request.POST.get('cpass')
    if check_password(cp, u.password):
        u.pic.delete()
        u.delete()
        return redirect('acc:index')
    return redirect('acc:profile')

def signup(request):
    if request.method == "POST":
        un = request.POST.get("uname")
        up = request.POST.get("upass")
        co = request.POST.get("com")
        pi = request.FILES.get("pic")
        try:
            User.objects.create_user(username=un, password=up, comment=co, pic=pi)
            return redirect("acc:login")
        except:
            pass
    return render(request, 'acc/signup.html')

def update(request):
    if request.method == "POST":
        u = request.user
        um = request.POST.get("umail")
        co = request.POST.get("com")
        pi = request.FILES.get("pic")
        u.email, u.comment= um, co
        if pi:
            u.pic.delete()
            u.pic = pi
        u.save()
        return redirect('acc:profile')
    return render(request, 'acc/update.html')

def chpass(request):
    u = request.user
    cp = request.POST.get("cpass")
    if check_password(cp, u.password):
        np = request.POST.get("npass")
        u.set_password(np)
        u.save()
        return redirect('acc:login')
    else:
        pass
        return redirect("acc:update")