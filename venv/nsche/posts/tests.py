from django.test import TestCase, Client
from .models import Post
from . import views
from django.urls import reverse
# Create your tests here.


# models tests
class PostModelTest(TestCase):
	""" Tests for the registration model """

	@classmethod
	def setUpTestData(cls):
		# Set up test data for the whole site
		cls.post = Post.objects.create(author='Orlando Julius James', matric_no='che/2013/051',
					title='Lorem Ipsum', body='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod.')

	
	def test_get_absolute_url(self):
		post=Post.objects.get(id=1)
		#This will also fail if the urlconf is not defined.
		self.assertEquals(post.get_absolute_url(),
				reverse('reatrix:post_detail', args=(self.post.id,)))


# view tests
class PostViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Set up test data for the whole site
		cls.post = Post.objects.create(author='Orlando Julius James', matric_no='che/2013/051',
					title='Lorem Ipsum', body='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod.')

		#cls.comments = Post.comments_set.create()

	def test_detail_view(self):
		response = self.client.get(reverse('reatrix:post_detail', args=(self.post.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, views.post_detail)
		self.assertEqual(response.context['post'], self.post)


