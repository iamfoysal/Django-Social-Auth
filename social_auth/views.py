from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from allauth.socialaccount.models import SocialAccount



class Home(TemplateView):
    template_name = "home.html"


def TotalUsers(request):
    total_users = User.objects.all().count()
    user_list = User.objects.all()
    social_account_list = SocialAccount.objects.all() # here is user profile data from social account


    context = {"total_users": total_users, "users": user_list}

    return render(request, "user_list.html", context)
