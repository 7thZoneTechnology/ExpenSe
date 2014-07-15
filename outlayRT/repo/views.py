from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from repo.models import Repo, Expenses
from repo.forms import ExpenseForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

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

def register(request):
	context = RequestContext(request)
	registered = False
	if request.method == 'POST':
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password) #this line hashes the password
			user.save()
			profile = profile_form.save(commit=False) #since user attribute needs to be set manually
			profile.user = user # set manually here
			if 'picture' in request.FILES:
				profile.picture = request.FILES['picture']
			profile.save()
			registered = True

		else:
			print user_form.errors, profile_form.errors
	else:
		user_form = UserForm()
		profile_form = UserProfileForm()
	return render_to_response('repo/register.html', 
		{'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, 
		context)

def user_login(request):
	context = RequestContext(request)
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				login(request, user )
				return HttpResponseRedirect('/OutlayRT/')
			else:
				return HttpResponse("Your Outlay account has been disabled")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render_to_response('repo/login.html', {}, context) 

@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/OutlayRT/')

	
