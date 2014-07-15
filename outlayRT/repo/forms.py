from django import forms
from repo.models import Expenses, Repo, UserProfile
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
	date = forms.CharField(max_length=64, help_text="Enter the date") #what date the expense was entered
	#description = forms.CharField(max_length=128, widget=forms.HiddenInput()) #description of the expense
	category = forms.CharField(max_length=64, help_text="Enter the category") #what category the description is a part of
	amount = forms.IntegerField(help_text="Enter the amount")
	repo = forms.CharField(max_length=32, help_text="Enter the repo") #name of the repo
	name = forms.CharField(max_length=32, help_text="Enter the expense")

	class Meta:
		model = Expenses
		fields = ('amount', 'repo', 'name')

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')

