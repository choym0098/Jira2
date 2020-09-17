# -*- coding: utf-8 -*-
from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["password_verification"]:
            user = User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                first_name=request.POST["first_name"],
                last_name=request.POST["last_name"],
                password=request.POST["password"],
            )
            auth.login(request, user)
            return redirect("home")
    return render(request, "jira2app/signup.html")
