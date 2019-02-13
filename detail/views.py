from django.shortcuts import render

# Create your views here.
def mysite(request):
    return render(request, "detail/mysite.html")

def qna(request):
    return render(request, "detail/qna.html")

def mypage(request):
    return render(request, "detail/mypage.html")

def signup(request):
    return render(request, "detail/signup.html")
    
def error(request, not_found):
    return render(request, "detail/error.html",{"not_found":not_found})
