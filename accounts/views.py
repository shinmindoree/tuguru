from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout

def logout(request):
    auth_logout(request)
    return redirect('posts:list')

def login(request):
    if request.method == 'POST':
        #데이터 수신
        username = request.POST['username']
        password = request.POST['password']
        #데이터 베이스 사용자 확인
        user = authenticate(request, username=username, password=password)
        #로그인처리
        if user:
            auth_login(request, user)
            return redirect('posts:list')
        else:
            context = {'error' : '아이디 또는 비밀번호가 틀렸습니다'}
            return render(request, 'accounts/login.html', context)
        #응답
        
    else:
        return render(request, "accounts/login.html")

def signup(request):
    if request.method == 'POST':
        #데이터 수신
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        #데이터 생성
        if password==password1:
            User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            #응답
            return redirect('posts:list')
        else:
            context = {"error" : '비밀번호 확인이 일치하지 않습니다.'}
            return render(request, 'accounts/signup.html', context)
    else:
        return render(request, 'accounts/signup.html')
