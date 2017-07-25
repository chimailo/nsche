from . import views
from django.conf.urls import url

app_name = 'users'

urlpatterns = [
		# /users/edit/pk/
		url(r'^edit/(?P<pk>[0-9]+)/$', views.edit_user, name='edit_user'),	
		# /users/register/
		url(r'^register/$', views.register, name='register_user'),
		# /users/part/1
		url(r'^part/1/$', views.part1_list, name='part1list'),
		# /users/part/2
		url(r'^part/2/$', views.part2_list, name='part2list'),
		# /users/part/3
		url(r'^part/3/$', views.part3_list, name='part3list'),
		# /users/part/4
		url(r'^part/4/$', views.part4_list, name='part4list'),
		# /users/part/fyb
		url(r'^part/5/$', views.part5_list, name='part5list'),
]