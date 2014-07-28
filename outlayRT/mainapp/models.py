from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Repo(models.Model):
	#user_id = models.ForeignKey(User)
	name = models.CharField(max_length=32, default="personal") #name of the repo
	username = models.CharField(max_length=32, unique=False) #who the repo belongs to
	PUBLIC_CHOICE = (
		('Y', 'Yes'),
		('N', 'No'),
		)
	public = models.CharField(max_length=1, choices=PUBLIC_CHOICE)
	def __unicode__(self):
		return self.name


class Expenses(models.Model):
	#user_id = models.ForeignKey(User)
	date = models.DateField(null=True) #what date the expense was entered
	description = models.CharField(max_length=128, null=True) #description of the expense
	category = models.CharField(max_length=64) #what category the description is a part of
	amount = models.IntegerField()
	repo = models.CharField(max_length=32) #name of the repo
	name = models.CharField(max_length=32)

	def __unicode__(self):
		return self.name

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	website = models.URLField(blank=True)
	picture = models.ImageField(upload_to='profile_images', blank=True)
	def __unicode__(self):
		return self.user.username

class Macros(models.Model):
	#user_id = models.ForeignKey(User)
	username = models.CharField(max_length=32, null=True) #who entered this expense
	key = models.CharField(max_length=1)
	value = models.CharField(max_length=32)
	standard = models.BooleanField()
	def __unicode__(self):
		return self.key





