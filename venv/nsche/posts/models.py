from __future__ import unicode_literals
from django.db import models
import datetime
from users.models import CustomUser
from django.core.urlresolvers import reverse
# Create your models here.


class Post(models.Model):
	author = models.CharField(max_length=50)
	title = models.CharField(max_length=100)
	matric_no = models.ForeignKey(CustomUser, max_length=12, on_delete=models.CASCADE)
	date_created = models.DateField('date published', auto_now_add=True)
	pub_date = models.DateField('date published', blank=True, null=True)
	body = models.TextField()

	
	def __str__(self):
		return self.title

	def publish(self):
	    self.pub_date = datetime.date.today()
	    self.save()

	def get_absolute_url(self):
		return reverse('posts:post_detail', kwargs={'pk':self.pk})


# class Comments(models.Model):
# 	article = models.ForeignKey('reatrix.Article', on_delete=models.CASCADE)
# 	name = models.CharField(max_length=50)
# 	matric_no = models.CharField(max_length=12)
# 	comment = models.TextField()
# 	comment_date = models.DateField(auto_now_add=True)

# 	def __str__(self):
# 		return self.comment

