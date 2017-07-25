from django import forms
from reatrix.models import Comments, Article


class CommentForm(forms.ModelForm):
	
	class Meta:
		model = Comments
		exclude = ['article', 'comment_date',]


class ArticleForm(forms.ModelForm):

	class Meta:
		model = Article
		exclude = ['date_created', 'pub_date', ]
