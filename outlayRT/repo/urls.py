from django.conf.urls import patterns, url
from repo import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^add_expense/$', views.add_expense, name='add_expense'),
	url(r'^(?P<repo_name_url>\w+)/$', views.repo, name='repo'),
	)