import os

standard_macros = { 'g': 'groceries',
			'c': 'car',
			'u': 'utilities',
			'f': 'food',
			'e': 'entertainment',
			'p': 'phone',
			}

def populate():
	for x in range(3):
		Repo.objects.get_or_create(name="repo" + str(x), username="username", public="N")
	#add test user
	User.objects.get_or_create(username="testuser", password="password", email="rhc245@gmail.com", first_name="test", last_name="user")
	#add standard macros
	for key, value in standard_macros.iteritems():
		Macros.objects.get_or_create(key=key, value=value, standard=True)

if __name__ == "__main__" :
	print "Starting outlay population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OutlayRT.settings')
	from mainapp.models import Repo, Expenses, Macros, UserProfile
	from django.contrib.auth.models import User
	populate()
