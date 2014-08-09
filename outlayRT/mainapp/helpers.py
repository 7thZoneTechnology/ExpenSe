from mainapp.models import Expenses, Macros, UserProfile, Budget
from django.contrib.auth.models import User

def checkIfExpense(request):
	for item in request:
		if item.isdigit():
			return item
	return False

def checkIfMacro(request):
	for item in request:
		if len(item) == 1:
			return item
	return False

def getRemaining():
	'''returns amount
	of budget left this month
	'''
	pass

def getAmountType(type, start_date):
	'''for a type of expense 
	gets the amount spent on that expense
	from the start_date
	'''
	pass