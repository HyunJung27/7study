from django.shortcuts import render, redirect
from django.contrib.auth.models import User #User에 대한 클래스를 가져온다.
from django.contrib import auth #계정의 권한에 대한 내용을 가져온다.

# Create your views here.
def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(Request, 'signup.html', {'error':'Username has already been taken'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user) #회원가입 후 자동으로 로그인
            return redirect('show')
        else:
            return render(request, 'signup.html', {'error':'Passwords must match'})
    else:
        return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('show')
        else:
            return render(request, 'login.html', {'error':'username or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('show')
    return render(request, 'show.html')
