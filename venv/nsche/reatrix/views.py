from .models import Article, Comments
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import datetime
from django.shortcuts import get_object_or_404, redirect, render
from .forms import CommentForm, ArticleForm

# Create your views here.

class ArticleList(ListView):
	model = Article
	context_object_name = 'articles'
	template_name = 'reatrix/all_articles.html'

	def get_queryset(self):
		articles = Article.objects.filter(pub_date__isnull=False)
		return articles.filter(pub_date__lte=datetime.date.today()).order_by('-pub_date')


class ArticleCreate(LoginRequiredMixin, CreateView):
	model = Article
	fields = ['author', 'title', 'matric_no', 'body']
	template_name = 'reatrix/add_article.html'
	login_url = '/login/'


def article_detail(request, pk):
	article = get_object_or_404(Article, pk=pk)
	comments = article.comments_set.all().order_by('-created_date')

	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.article = article
			comment.comment_date = datetime.date.today()
			comment.save()
			redirect('reatrix:all_articles')
	else:
		form = CommentForm()

	return render(request, 'reatrix/article_detail.html', {'article': article, 
														'comments': comments,
														'form': form})


class ArticleUpdate(LoginRequiredMixin, UpdateView):
	model = Article
	fields = ['author', 'title', 'matric_no', 'body']
	template_name = 'reatrix/add_article.html'
	login_url = '/login/'


def draft_list(request):
    articles = Article.objects.filter(pub_date__isnull=True).order_by('date_created')
    return render(request, 'reatrix/draft_list.html', {'articles': articles})


@permission_required('reatrix.add_article', login_url='/login')
def publish_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.publish()
    return redirect('reatrix:all_articles')


class ArticleDelete(PermissionRequiredMixin, DeleteView):
	model = Article
	success_url = reverse_lazy('reatrix:draft_list')
	permission_required = 'reatrix.delete_article'
	login_url='/login'