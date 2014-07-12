from django.db import models

# Create your models here.

class Repo(models.Model):
	name = models.CharField(max_length=32, default="personal") #name of the repo
	username = models.CharField(max_length=32, unique=False) #who the repo belongs to
	public = models.BooleanField(default=True)

	def __unicode__(self):
		return "This is the repo table"


class Expenses(models.Model):
	username = models.CharField(max_length=32) #who entered this expense
	date = models.DateField(null=True) #what date the expense was entered
	description = models.CharField(max_length=128, null=True) #description of the expense
	category = models.CharField(max_length=64) #what category the description is a part of
	amount = models.IntegerField()
	repo = models.CharField(max_length=32) #name of the repo
	name = models.CharField(max_length=32)

	def __unicode__(self):
		return "This is the expenses table"




