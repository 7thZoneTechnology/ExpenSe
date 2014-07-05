from django.db import models

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=32, unique=True)
	password = models.CharField(max_length=16, unique=False, null=True)
	mytext = models.CharField(max_length=128, unique=False, null=True)
	date = models.DateField(null=True)
	userid = models.IntegerField(null=True)

	def __unicode__(self):
		return self.username