from django import forms
from .models import Post


# class CommentForm(forms.ModelForm):
	
# 	class Meta:
# 		model = Comments
# 		exclude = ['article', 'comment_date',]


class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ['title','body']

		widgets = {'body': forms.Textarea(attrs={'class':'materialize-textarea'})}