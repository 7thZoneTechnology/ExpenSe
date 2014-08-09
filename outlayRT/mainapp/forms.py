from django import forms
from mainapp.models import Expenses, UserProfile, Macros, Budget
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
	date = forms.DateTimeField(required=False, widget=forms.HiddenInput()) #what date the expense was entered
	description = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False) #description of the expense
	user_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
	name = forms.CharField(max_length=64, required=False, help_text="") # ex. groceries, entertainment, etc.
	amount = forms.IntegerField(required=False, widget=forms.HiddenInput())

	class Meta:
		model = Expenses
		fields = ('amount', 'name', 'description')

class MacroForm(forms.ModelForm):
	key = forms.CharField(max_length=1, widget=forms.HiddenInput(), required=False)
	value = forms.CharField(max_length=32, help_text="")
	user_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
	standard = forms.BooleanField(widget=forms.HiddenInput(), required=False)
	class Meta:
		model = Macros
		fields = ('key', 'value')

class ExpenseEditForm(forms.ModelForm):
	date = forms.DateTimeField(required=False, help_text="Date") #what date the expense was entered
	description = forms.CharField(max_length=128, required=False, help_text="Description") #description of the expense
	name = forms.CharField(max_length=64, required=False, help_text="Name") # ex. groceries, entertainment, etc.
	amount = forms.IntegerField(required=False, help_text="Amount")

	class Meta:
		model = Expenses
		fields = ('amount', 'date', 'name', 'description')

class BudgetForm(forms.ModelForm):
	input = forms.CharField(max_length=10, required=False, help_text="Input")
	create_date = forms.DateField(widget=forms.HiddenInput(), required=False)
	class Meta:
		model = Budget
		fields = ('input', 'create_date')

# User forms

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')


