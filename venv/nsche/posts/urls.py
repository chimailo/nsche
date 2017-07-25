from . import views
from django.conf.urls import url

app_name = 'posts'

urlpatterns = [
		url(r'^all/$', views.PostList.as_view(), name='all_posts'),
		url(r'^(?P<pk>\d+)/$', views.PostDetail.as_view(), name='post_detail'),
		url(r'^add/$', views.create_post, name='add_post'),
		url(r'^edit/(?P<pk>\d+)/$', views.PostUpdate.as_view(), name='post_edit'),
		url(r'^del/(?P<pk>\d+)/$', views.PostDelete.as_view(), name='post_delete'),
		url(r'^drafts/$', views.draft_list, name='draft_list'),
		url(r'^article/(?P<pk>\d+)/publish/$', views.publish_post, name='publish_post'),

		# url(r'^like/(?P<pk>\d+)/$', views.like_article, name='like_article'),
]