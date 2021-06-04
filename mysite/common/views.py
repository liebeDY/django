from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from common.forms import UserForm

# Create your views here.
def signup(request):
    """
    계정생성
    """
    if request.method == "POST":    # POST 요청 : 입력한 데이터로 새로운 사용자 생성
        form = UserForm(request.POST)
        if form.is_valid(): # UserCreationForm의 is_valid 함수 : 필드값 3개가 모두 입력되었는지, password1과 password2가 같은지, 비밀번호 생성 규칙에 맞는지 등을 검사 
            form.save()
            username = form.cleaned_data.get('username')    # form.cleaned_data.get 함수 : 회원가입 화면에서 입력한 값을 얻기 위해 사용하는 함수 
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)   # 사용자 인증
            login(request, user)    # 회원가입 이후 자동 로그인
            return redirect('index')
    else:   # GET 요청 : common/signup.html 화면 반환
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})