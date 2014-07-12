
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from repo.models import Repo, Expenses
from repo.forms import ExpenseForm

def index(request): #render the index page
	context = RequestContext(request)
	repo_list = Repo.objects.order_by('name')
	for repo in repo_list:
		repo.url = repo.name.replace(' ' , '_')
	context_dict = {'repos': repo_list}
	return render_to_response('repo/index.html', context_dict, context)

def repo(request, repo_name_url): #render each individual repo's page
	context = RequestContext(request)
	repo_name = repo_name_url.replace("_", " ")
	context_dict = {'repo_name': repo_name}
	try:
		public = Repo.objects.get(name=repo_name).public
		expense_list = Expenses.objects.filter(repo=repo_name)
		context_dict['public'] = public
		context_dict['expenses'] = expense_list
	except Repo.DoesNotExist:
		pass
	return render_to_response('repo/repo.html', context_dict, context)

def add_expense(request):
	context = RequestContext(request)
	if request.method =='POST':
		form = ExpenseForm(request.POST)
		if form.is_valid():
			print "Test"
			form.save(commit=True) #this line isn't working
			print "Test"
			return index(request)
		else:
			print form.errors
	else:
		form = ExpenseForm()
	return render_to_response('repo/add_expense.html', {'form': form}, context)
