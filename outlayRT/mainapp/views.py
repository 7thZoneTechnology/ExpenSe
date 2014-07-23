from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from mainapp.models import Repo, Expenses
from mainapp.forms import ExpenseForm, UserForm, UserProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime

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
	for repo in repo_list:
		repo.url = repo.name.replace(' ' , '_')
	context_dict = {'repos': repo_list}
	return render_to_response('mainapp/dashboard.html', context_dict, context)

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
	return render_to_response('mainapp/repo.html', context_dict, context)

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

	
