from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from mainapp.forms import ExpenseForm, UserForm, UserProfileForm, MacroForm, ExpenseEditForm, BudgetForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from helpers import checkIfExpense, checkIfMacro, getBudgetUsed, costPerDay
from crud import createExpense, createMacro, readExpense, readMacro, deleteExpense, deleteMacro, updateExpense, updateMacro, readBudget, createBudget, deleteBudget

@login_required
def dashboard(request, user_name_url): 
	context = RequestContext(request)
	user_name = user_name_url.replace("_", " ")

	context_dict = {'macros': readMacro(user_name)}
	if request.method =='POST':
		if 'budget' in request.POST:
			budget_form = BudgetForm(request.POST)
			if budget_form.is_valid():
				final_form = budget_form.save(commit=False)
				if createBudget(budget_form.cleaned_data['input'], final_form, user_name):
					final_form.save()
			else:
				print budget_form.errors
		elif 'expense' in request.POST:
			expense_form = ExpenseForm(request.POST)
			if expense_form.is_valid():
				final_form = expense_form.save(commit=False)
				createExpense(expense_form.cleaned_data['name'], macros, user_name, final_form) 
				final_form.save()
			else:
				print expense_form.errors
		elif 'macro' in request.POST:
			macro_form = MacroForm(request.POST)
			if macro_form.is_valid():
				final_form = macro_form.save(commit=False)				
				user_input = macro_form.cleaned_data['value']
				# user cannot delete pre-set macros
				if not createMacro(macro_form.cleaned_data['value'], user_name, final_form):
					final_form.save() 
			else:
				print macro_form.errors
		elif 'delete_budget' in request.POST:
			deleteBudget(user_name)
		elif checkIfExpense(request.POST):
			deleteExpense(checkIfExpense(request.POST))
		elif checkIfMacro(request.POST):
			deleteMacro(checkIfMacro(request.POST), user_name)
	context_dict['used'] = getBudgetUsed(user_name)
	context_dict['budget'] = readBudget(user_name)
	context_dict['percentage'] = str(getBudgetUsed(user_name)/readBudget(user_name).budget).split('.')[1][:2]
	context_dict['perday'] = costPerDay(user_name)
	context_dict['expenses'] = readExpense("filter", user_name=user_name)
	context_dict['macros'] = readMacro(user_name)
	context_dict['budget_form'] = BudgetForm()
	context_dict['expense_form'] = ExpenseForm()
	context_dict['macro_form'] = MacroForm()
	return render_to_response('mainapp/dashboard.html', context_dict, context)

@login_required
def edit_expense(request, user_name_url, expense_id_url):
	context = RequestContext(request)
	user_name = user_name_url.replace('_', ' ')
	expense_id = expense_id_url.replace('_', ' ')
	
	if request.method =='POST':
		if 'expense' in request.POST:
			expense_form = ExpenseForm(request.POST)
			if expense_form.is_valid():
				final_form = expense_form.save(commit=False)
				updateExpense(expense_form, expense_id)
			else:
				print expense_form.errors

	expense = readExpense("get", id=expense_id)
	context_dict = {'expense' : expense}

	expense_form = ExpenseEditForm()
	context_dict['expense_form'] = expense_form

	return render_to_response('mainapp/edit_expense.html', context_dict, context)



def index(request): 
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


# User registration and login views

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

	
