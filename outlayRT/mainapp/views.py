from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from mainapp.models import Repo, Expenses, Macros
from mainapp.forms import ExpenseForm, UserForm, UserProfileForm, RepoForm, MacroForm 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

#def decode(coded):


def index(request): #render the index page
	context = RequestContext(request)
	response = render_to_response('mainapp/index.html', context)
	if request.session.get('last_visit'):
		last_visit_time = request.session.get('last_visit')
		visits = request.session.get('visits', '0')
		if (datetime.now() - datetime.strptime(last_visit_time[:-7], "%Y-%m-%d %H:%M:%S")).seconds > 5:
			request.session['visits'] = visits + 1
			request.session['last_visit'] = str(datetime.now())
	else:
		request.session['last_visit'] = str(datetime.now())
		request.session['visits'] = 1
	return response


def dashboard(request, user_name_url): #render the index page
	context = RequestContext(request)
	user_name = user_name_url.replace("_", " ")
	repo_list = Repo.objects.filter(username=user_name)
	standard_list = Macros.objects.filter(standard=True) # standard list of macros
	#macro_list = Macros.objects.filter(user=user_name) # user list of macros
	#for standard in standard_list:
	#	for item in macro_list:
	#		if item.key == standard.key:
	#			standard.value = item.value
	macros = standard_list
	context_dict = {'macros': macros}
	for repo in repo_list:
		repo.url = repo.name.replace(' ' , '_')
	context_dict['repos'] = repo_list
	if request.method =='POST':
		if 'expense' in request.POST:
			expense_form = ExpenseForm(request.POST)
			if expense_form.is_valid():
				expense_form.save(commit=False) 
				parse_this = expense_form.cleaned_data['name'] #this is how I get the form input string
				repo_form = RepoForm()
			else:
				print expense_form.errors
		elif 'repo' in request.POST:
			print 'repo'
			repo_form = RepoForm(request.POST)
			if repo_form.is_valid():
				name = repo_form.cleaned_data['name'] #this is how you get data
				final_form = repo_form.save(commit=False)
				final_form.username = user_name
				final_form.public = 'N'
				final_form.save()
				expense_form = ExpenseForm()
			else:
				print repo_form.errors
	else:
		expense_form = ExpenseForm()
		repo_form = RepoForm()
	context_dict['expense_form'] = expense_form
	context_dict['repo_form'] = repo_form
	return render_to_response('mainapp/dashboard.html', context_dict, context)

def repo(request, user_name_url, repo_name_url): #render each individual repo's page
	context = RequestContext(request)
	repo_name = repo_name_url.replace("_", " ")
	user_name = user_name_url.replace("_", " ")
	context_dict = {'repo_name': repo_name}
	context_dict['user_name'] = user_name
	try:
		repo_list = Repo.objects.get(username=user_name)
		for repo in repo_list:
			if repo.name == repo_name:
				expense_list = Expenses.objects.filter(repo=repo_name)		
				context_dict['expenses'] = expense_list #only gets expenses in repo if repo belongs to user
	except Repo.DoesNotExist:
		pass
	return render_to_response('mainapp/repo.html', context_dict, context)

def add_expense(request):
	context = RequestContext(request)
	if request.method =='POST':
		form = ExpenseForm(request.POST)
		if form.is_valid():
			form.save(commit=True) #this line isn't working
			return index(request)
		else:
			print form.errors
	else:
		form = ExpenseForm()
	return render_to_response('mainapp/add_expense.html', {'form': form}, context)

def add_repo(request):
	context = RequestContext(request)
	if request.method == 'POST':
		form = RepoForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return index(request)
		else:
			print form.errors
	else: 
		form = ExpenseForm()
	return render_to_response('mainapp/add_expense.html', {'form': form}, context)


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
	return render_to_response('mainapp/register.html', 
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
				return HttpResponseRedirect('/OutlayRT/' + username)
			else:
				return HttpResponse("Your Outlay account has been disabled")
		else:
			print "Invalid login details: {0}, {1}".format(username, password)
			return HttpResponse("Invalid login details supplied.")
	else:
		return render_to_response('mainapp/login.html', {}, context) 

@login_required
def restricted(request):
	return HttpResponse("Since you're logged in, you can see this text!")

@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect('/OutlayRT/')

	
