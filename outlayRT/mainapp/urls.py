from django.conf.urls import patterns, url
from mainapp import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^add_expense/$', views.add_expense, name='add_expense'),
	url(r'^add_repo/$', views.add_repo, name='add_repo'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^(?P<user_name_url>\w+)/$', views.dashboard, name='dashboard'),
	url(r'^(?P<user_name_url>\w+)/(?P<repo_name_url>\w+)/$', views.repo, name='repo'),
	)