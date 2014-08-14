import django_tables2 as tables
from mainapp.models import Expenses

class ExpenseTable(tables.Table):
	class Meta:
		model = Expenses
		# add class="paleblue" to <table> tag
		fields = ('name', 'amount', 'date', 'description', 'edit')
		attrs = {"class": "table"}