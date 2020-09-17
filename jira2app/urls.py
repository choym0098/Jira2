# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = "jira2app"
# view나 template에서 해당 이름을 이용해 url에 요청을 보낼 수 있다.

urlpatterns = [
    path("sign_up/", views.sign_up, name="sign_up"),
    # "<내 URL>/jira2app/sign_up/" 주소로 요청이 오면 views.py 안에 sign_up이라는 함수를 찾아 실행한다.
]
