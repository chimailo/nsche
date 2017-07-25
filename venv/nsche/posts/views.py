from .models import Post
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import DeleteView, UpdateView
from django.conf import settings
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .forms import PostForm

# Create your views here.

class PostList(ListView):
	model = Post
	context_object_name = 'posts'
	template_name = 'posts/all_posts.html'

	def get_queryset(self):
		posts = Post.objects.filter(pub_date__isnull=False)
		return posts.filter(pub_date__lte=datetime.date.today()).order_by('-pub_date')


class PostDetail(DetailView):
	model = Post
	context_object_name = 'post'
	template_name = 'posts/post_detail.html'


@login_required()
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user.get_full_name()
            post.matric_no = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'posts/add_post.html', {'form': form})


class PostUpdate(PermissionRequiredMixin, UpdateView):
	model = Post
	template_name = 'posts/edit_post.html'
	login_url = '/login'
	permission_required = 'post.add_post'
	form_class = PostForm


def draft_list(request):
    posts = Post.objects.filter(pub_date__isnull=True).order_by('date_created')
    return render(request, 'posts/all_posts.html', {'posts': posts})


@permission_required('post.add_post', login_url='/login')
def publish_post(request, pk):
    post = get_object_or_404(Article, pk=pk)
    post.publish()
    return redirect('post:all_posts')


class PostDelete(PermissionRequiredMixin, DeleteView):
	model = Post
	success_url = reverse_lazy('post:draft_list')
	permission_required = 'post.delete_post'
	login_url='settings.LOGIN_URL'