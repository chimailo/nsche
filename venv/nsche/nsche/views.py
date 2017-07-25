from django.shortcuts import render, redirect
from users.forms import UserCreationForm
from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse
from django.core import serializers
from users.models import CustomUser
from posts.models import Post
from datetime import date

def home(request):
	post_all = Post.objects.filter(pub_date__isnull=False)
	posts = post_all.filter(pub_date__lte=date.today()).order_by('-pub_date')[:5]
	excos= CustomUser.objects.filter(is_exco=True)
	context = {'posts':posts, 'excos':excos,}
	return render(request, 'home.html', context)


def logout_view(request):
    logout(request)
    return redirect("home")


