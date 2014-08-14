from mainapp.models import Expenses, Macros, UserProfile, Budget
from django.contrib.auth.models import User
from datetime import datetime, date
from monthdelta import MonthDelta
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist
import re
from dateutil import parser

def createExpense(coded, macros, user_name, final_form):
	'''
	Parses the user input for an expense and and prepares
	final_form to be stored	into database
	'''
	result = {}
	# optional name, user can update later
	decoded = re.compile(r'([^.0-9]*)?(\d*\.?\d*)?(\D*)?')
	name = decoded.search(coded).groups()[0]
	if name in macros.keys():
		name = macros[name]
	final_form.name = name
	# get amount
	if len(decoded.search(coded).groups()[1]) > 0:
		amount = float(decoded.search(coded).groups()[1])
	else:
		amount  = 0
	final_form.amount = amount
	# optional description, user can update later
	final_form.description = decoded.search(coded).groups()[2]
	# get date
	date = datetime.now()
	final_form.date = date
	final_form.month = date.month
	# get user id
	final_form.user_id = getUserId(user_name)

def readExpense(command, user_name=None, id=None):
	if command == "filter":
		return Expenses.objects.filter(user_id=getUserId(user_name)).order_by('-date')
	elif command == "get":
		try:
			return Expenses.objects.get(expense_id__exact=id)
		except ObjectDoesNotExist:
			return None
	elif command.substring("month"):
		return Expenses.objects.filter(user_id=getUserId(user_name)).order_by('-date')

def updateExpense(form , id):
	expense = Expenses.objects.get(expense_id=id)
	if form.cleaned_data['amount']:
		expense.amount = form.cleaned_data['amount']
	if form.cleaned_data['date']:
		expense.date = parser.parse(form.cleaned_data['date'])
		expense.month = expense.date.month
	if form.cleaned_data['name']:
		expense.name = form.cleaned_data['name']
	if form.cleaned_data['description']:
		expense.description = form.cleaned_data['description']
	expense.save()

def deleteExpense(id):
	expense = Expenses.objects.get(expense_id__exact=id)
	expense.delete()

def createMacro(user_input, user_name, final_form):
	'''
	Parses the user input for a macro and prepares 
	final_form to be created in the database
	'''
	final_form.key = user_input[0]
	
	final_form.user_id = getUserId(user_name)
	final_form.value = user_input[1:]
	try:
		Macros.objects.get(Q(key__exact=user_input[0]) & Q(user_id__exact=getUserId(user_name)))
		return True
	except ObjectDoesNotExist:
		return False

def readMacro(user_name):
	'''
	Returns a dictionary of standard and user set
	macros with user set macros overwriting standard ones
	'''
	macros = {}
	standard_list = Macros.objects.filter(user_id=None) # standard list of macros
	
	macro_list = Macros.objects.filter(user_id=getUserId(user_name)) # user list of macros
	for item in macro_list:
		macros[item.key] = item.value
	for item in standard_list:
		if item.key not in macros:
			macros[item.key] = item.value
	return macros

def createBudget(user_input, final_form, user_name):
	if readBudget(user_name):
 		return updateBudget(readBudget(user_name), user_input)
	final_form.create_date = date.today()
	final_form.latest_date = date.today() + MonthDelta(1)
	try:
		final_form.budget = float(user_input)
	except ValueError:
		return False
	final_form.user_id = getUserId(user_name)
	return True

def readBudget(user_name):
	'''returns a tuple
	of budget, budget_date
	for a given user'''
	try:
		budget = Budget.objects.get(user_id=getUserId(user_name))
		today = date.today()
		if (today == budget.latest_date):
			budget.latest_date = today + MonthDelta(1)
			budget.save()
		return Budget.objects.get(user_id=getUserId(user_name))
	except ObjectDoesNotExist:
		return None
	
def updateBudget(budget, user_input):
	try:
		budget.budget = float(user_input)
	except ValueError:
		return False
	budget.save()
	return True

def deleteBudget(user_name):
	budget = Budget.objects.get(user_id=getUserId(user_name))
	budget.delete()
	
	

def updateMacro():
	pass


def deleteMacro(key, username):
	# print key, getUserId(username)
	try:
		macro = Macros.objects.get(Q(key__exact=key), Q(user_id=getUserId(username)))
		macro.delete()
	except ObjectDoesNotExist:
		print "Preset"
	
# helper functions
def getUserId(user_name):
	return UserProfile.objects.get(user__username=user_name)



