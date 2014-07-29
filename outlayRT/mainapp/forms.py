from django import forms
from mainapp.models import Expenses, Repo, UserProfile, Macros
from django.contrib.auth.models import User

class ExpenseForm(forms.ModelForm):
	date = forms.CharField(max_length=64, required=False, widget=forms.HiddenInput()) #what date the expense was entered
	#description = forms.CharField(max_length=128, widget=forms.HiddenInput()) #description of the expense
	category = forms.CharField(max_length=64, required=False, widget=forms.HiddenInput()) # ex. groceries, entertainment, etc.
	amount = forms.IntegerField(required=False, widget=forms.HiddenInput())
	repo = forms.CharField(max_length=32, required=False, widget=forms.HiddenInput()) #name of the repo

	class Meta:
		model = Expenses
		fields = ('amount', 'repo', 'name')

class RepoForm(forms.ModelForm):
	name = forms.CharField(max_length=64, help_text="")
	username = forms.CharField(max_length=128, widget=forms.HiddenInput(), required=False)
	public = forms.CharField(max_length=1, widget=forms.HiddenInput(), required=False)
	class Meta:
		model = Repo
		fields = ('name', )
class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'password', 'email')

class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ('website', 'picture')

class MacroForm(forms.ModelForm):
	key = forms.CharField(max_length=32, help_text="")
	value = forms.CharField(max_length=1, widget=forms.HiddenInput(), required=False)
	username = forms.CharField(max_length=1, widget=forms.HiddenInput(), required=False)
	standard = forms.BooleanField(widget=forms.HiddenInput(), required=False)
	class Meta:
		model = Macros
		fields = ('key', 'value', 'standard', 'username')

