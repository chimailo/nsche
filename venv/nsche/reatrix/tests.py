from django.test import TestCase, Client
from .models import Article
from . import views
from django.urls import reverse
# Create your tests here.


# models tests
class ArticleModelTest(TestCase):
	""" Tests for the registration model """

	@classmethod
	def setUpTestData(cls):
		# Set up test data for the whole site
		cls.article = Article.objects.create(author='Orlando Julius James', matric_no='che/2013/051',
					title='Lorem Ipsum', body='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod.')

	
	def test_get_absolute_url(self):
		article=Article.objects.get(id=1)
		#This will also fail if the urlconf is not defined.
		self.assertEquals(article.get_absolute_url(),
				reverse('reatrix:article_detail', args=(self.article.id,)))


# view tests
class ArticleViewTest(TestCase):
	@classmethod
	def setUpTestData(cls):
		# Set up test data for the whole site
		cls.article = Article.objects.create(author='Orlando Julius James', matric_no='che/2013/051',
					title='Lorem Ipsum', body='Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod.')

		cls.comments = Article.comments_set.create()

	def test_detail_view(self):
		response = self.client.get(reverse('reatrix:article_detail', args=(self.article.id,)))
		self.assertEqual(response.status_code, 200)
		self.assertEqual(response.resolver_match.func, views.article_detail)
		self.assertEqual(response.context['article'], self.article)


