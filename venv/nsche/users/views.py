from django.shortcuts import render, redirect, get_object_or_404
from users.models import CustomUser
from users.forms import UserCreationForm, UserProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.views.generic.base import View
from django.conf import settings
# Create your views here.

def part1_list(request):
	class_list = CustomUser.objects.filter(part=100).order_by('matric_no')
	return render(request, 'users/part1list.html', {'class_list':class_list})
	
def part2_list(request):
	class_list = CustomUser.objects.filter(part=200).order_by('matric_no')
	return render(request, 'users/part2list.html', {'class_list':class_list})
	
def part3_list(request):
	class_list = CustomUser.objects.filter(part=300).order_by('matric_no')
	return render(request, 'users/part3list.html', {'class_list':class_list})
	
def part4_list(request):
	class_list = CustomUser.objects.filter(part=400).order_by('matric_no')
	return render(request, 'users/part4list.html', {'class_list':class_list})

def part5_list(request):
	class_list = CustomUser.objects.filter(part=500).order_by('matric_no')
	return render(request, 'users/part5list.html', {'class_list':class_list})
	

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid() and form.clean_matric_no():
            form.save()
            matric_no = form.cleaned_data.get('matric_no')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, matric_no=matric_no, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'registration/register.html', {'form': form})


@login_required()
def edit_user(request, pk):
	user = get_object_or_404(CustomUser, pk=pk)
	form = UserProfileForm(instance=user)
	if request.method == "POST":
		form = UserProfileForm(request.POST, request.FILES, instance=user)
		if request.user.pk == user.pk:
			if form.is_valid():
				form.save()
				return redirect('home')
		else:
			return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))


	return render(request, "users/edit_user.html", {'form':form})

