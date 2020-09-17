# -*- coding: utf-8 -*-
from django.contrib.auth import login as user_login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render


def sign_up(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user_login(request, user)
        return redirect("jira2app:sign_up")
    else:
        form = UserCreationForm()
        return render(request, "jira2app/form.html", {"form": form})
