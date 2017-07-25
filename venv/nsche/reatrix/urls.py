from . import views
from django.conf.urls import url

app_name = 'reatrix'

urlpatterns = [
		url(r'^all/$', views.ArticleList.as_view(), name='all_articles'),
		url(r'^(?P<pk>\d+)/$', views.article_detail, name='article_detail'),
		url(r'^add/$', views.ArticleCreate.as_view(), name='add_article'),
		url(r'^edit/(?P<pk>\d+)/$', views.ArticleUpdate.as_view(), name='article_edit'),
		url(r'^del/(?P<pk>\d+)/$', views.ArticleDelete.as_view(), name='article_delete'),
		url(r'^drafts/$', views.draft_list, name='draft_list'),
		url(r'^article/(?P<pk>\d+)/publish/$', views.publish_article, name='publish_article'),

		# url(r'^like/(?P<pk>\d+)/$', views.like_article, name='like_article'),
]