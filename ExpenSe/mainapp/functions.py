from mainapp.models import Expenses, Macros, UserProfile
from datetime import datetime
from django.db.models import Q
from django.core.exceptions import ObjectDoesNotExist

def createExpense(coded, macros, user_name, final_form):
	'''
	Parses the user input for an expense and and prepares
	final_form to be stored	into database
	'''
	result = {}
	# optional name, user can update later
	if not coded[0].isdigit():
		name = macros[coded[0]]
	else:
		name = None
	final_form.name = name
	# get amount
	amount = ""
	i = 1
	while i < len(coded) and (coded[i].isdigit() or coded[i] == '.'):
		amount += coded[i]
		i += 1
	amount = float(amount)
	final_form.amount = amount
	# optional description, user can update later
	description = coded[i:]
	final_form.description = description
	# get date
	date = datetime.now()
	final_form.date = date
	# get user id
	final_form.user_id = getUserId(user_name)

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

def readMacros(user_name):
	'''
	Returns a dictionary of standard and user set
	macros with user set macros overwriting standard ones
	'''
	macros = {}
	standard_list = Macros.objects.filter(standard=True) # standard list of macros
	
	macro_list = Macros.objects.filter(user_id=getUserId(user_name)) # user list of macros
	for item in macro_list:
		macros[item.key] = item.value
	for item in standard_list:
		if item.key not in macros:
			macros[item.key] = item.value
	return macros

def readExpenses(user_name=None, id=None, command):
	if command == "filter":
		return Expenses.objects.filter(user_id=getUserId(user_name))
	elif command =="get":
		return Expenses.objects.get(expense_id__exact=id)

def getUserId(user_name):
	return getUserId(user_name)

def checkIfExpense(request):
	for item in request:
		if item.isdigit():
			return item
	return False

def deleteExpense(id):
	expense = Expenses.objects.get(expense_id__exact=id)
	expense.delete()
	return

def checkIfMacro(request):
	for item in request:
		if len(item) == 1:
			return item
	return False

def deleteMacro(key, username):
	macro = Macros.objects.get(Q(key__exact=key), Q(username__exact=username))
	if macro.standard == False:
		macro.delete()
	return

def getExpenseInfo(id):
	return Expenses.objects.get(expense_id__exact=id)
