from django import forms
from mainapp.models import Expenses, UserProfile, Macros
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
	date = forms.CharField(max_length=64, required=False, widget=forms.HiddenInput()) #what date the expense was entered
	description = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False) #description of the expense
	username = forms.CharField(max_length=32, widget=forms.HiddenInput(), required=False)
	name = forms.CharField(max_length=64, required=False, help_text="") # ex. groceries, entertainment, etc.
	amount = forms.IntegerField(required=False, widget=forms.HiddenInput())
	repo = forms.CharField(max_length=32, required=False, widget=forms.HiddenInput()) #name of the repo

	class Meta:
		model = Expenses
		fields = ('amount', 'repo', 'name', 'description')

class MacroForm(forms.ModelForm):
	key = forms.CharField(max_length=1, widget=forms.HiddenInput(), required=False)
	value = forms.CharField(max_length=32, help_text="")
	username = forms.CharField(max_length=32, widget=forms.HiddenInput(), required=False)
	standard = forms.BooleanField(widget=forms.HiddenInput(), required=False)
	class Meta:
		model = Macros
		fields = ('key', 'value', 'standard', 'username')



class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')


