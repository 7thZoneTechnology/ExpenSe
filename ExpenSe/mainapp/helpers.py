from mainapp.models import Expenses, Macros, UserProfile, Budget
from django.contrib.auth.models import User
from crud import readMacro, readBudget, getUserId
from monthdelta import MonthDelta
from datetime import datetime

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

def getBudgetUsed(user_name):
	'''returns amount
	of budget used this month
	'''
	macros = readMacro(user_name)
	budget = readBudget(user_name)
	used = 0
	for k,v in macros.items():
		used += getExpenseAmount(v, user_name, budget.latest_date - MonthDelta(1))
	return used

def getExpenseAmount(name, user_name, start_date):
	'''for a type of expense 
	gets the amount spent on that expense
	from the start_date
	'''
	amount = 0
	expenses = Expenses.objects.filter(user_id__exact=getUserId(user_name),
		name__exact=name, date__gte=start_date)
	for item in expenses:
		amount += item.amount
	return amount

def costPerDay(user_name):
	amount = 0
	join_date = getUserId(user_name).user.date_joined.replace(tzinfo=None)
	today = datetime.now()
	days = (today - join_date).days + 1
	expenses = Expenses.objects.filter(user_id__exact=getUserId(user_name))
	for item in expenses:
		amount += item.amount
	if days == 0:
		return amount
	return amount/days

def getPercentage(user_name):
	fraction = getBudgetUsed(user_name)/readBudget(user_name).budget
	return fraction*100