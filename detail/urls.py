from django.urls import path
from . import views
from django.conf.urls import handler404

app_name = "details"
# handler404 = "detail.views.error404"



urlpatterns = [
    path("", views.mysite, name="mysite"),
    path("qna/", views.qna, name="qna"),
    path("mypage/", views.mypage, name="mypage"),
    path("signup/", views.signup, name="signup"),
    path("<str:not_found>/", views.error, name="error"),
    ]

