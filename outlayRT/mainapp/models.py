from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
	id = models.AutoField(primary_key=True)
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	def __unicode__(self):
		return self.user.username

class Expenses(models.Model):
	user_id = models.ForeignKey(UserProfile)
	expense_id = models.AutoField(primary_key=True)
	date = models.DateField(null=True) #what date the expense was entered
	description = models.CharField(max_length=128, null=True) #description of the expense
	amount = models.FloatField()
	name = models.CharField(max_length=32) 
	# repo = models.CharField(max_length=32) #name of the repo 
	def __unicode__(self):
		return self.name

class Macros(models.Model):
	user_id = models.ForeignKey(UserProfile, null=True)
	macro_id = models.AutoField(primary_key=True)
	key = models.CharField(max_length=1)
	value = models.CharField(max_length=32)
	# standard = models.BooleanField()
	def __unicode__(self):
		return self.key

class Budget(models.Model):
	# budget_id = models.AutoField(primary_key=True)
	user_id = models.ForeignKey(UserProfile, null=True)
	budget = models.FloatField(null=True)
	create_date = models.DateField(null=True)
	latest_date = models.DateField(null=True)
	def __unicode__(self):
		return "Budget"

'''
class Repo(models.Model):
	#user_id = models.ForeignKey(User)
	repo_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=32, default="personal") #name of the repo
	username = models.CharField(max_length=32, unique=False) #who the repo belongs to
	PUBLIC_CHOICE = (
		('Y', 'Yes'),
		('N', 'No'),
		)
	public = models.CharField(max_length=1, choices=PUBLIC_CHOICE)
	def __unicode__(self):
		return self.name
'''




