from django.shortcuts import render

# Create your views here.
def index(request): # request는 무조건 선언 필수
    # url로부터 호출되면
    # 메인 페이지 응답 객체르 만들어서 반환
    return render(request, 'index.html')

