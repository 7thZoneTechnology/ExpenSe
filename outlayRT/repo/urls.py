from django.conf.urls import patterns, url
from repo import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^add_expense/$', views.add_expense, name='add_expense'),
	url(r'^register/$', views.register, name='register'),
	url(r'^login/$', views.user_login, name='login'),
	url(r'^restricted/', views.restricted, name='restricted'),
	url(r'^logout/$', views.user_logout, name='logout'),
	url(r'^(?P<repo_name_url>\w+)/$', views.repo, name='repo'),
	)