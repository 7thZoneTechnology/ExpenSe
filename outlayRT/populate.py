import os

def populate():
	for x in range(25):
		User.objects.get_or_create(username="user"+str(x), mytext="testinguser"+str(x), userid=str(x))
	

if __name__ == "__main__" :
	print "Starting account population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OutlayRT.settings')
	from account.models import User
	populate()
