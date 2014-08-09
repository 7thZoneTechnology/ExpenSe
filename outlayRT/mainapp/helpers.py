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