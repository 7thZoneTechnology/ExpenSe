import os

def populate():
	for x in range(3):
		Repo.objects.get_or_create(name="repo" + str(x))
		for y in range(5):
			Expenses.objects.get_or_create(repo="repo" + str(x), amount=y+10, date= "2014-07-12", name="expense" + str(x*y))
	

if __name__ == "__main__" :
	print "Starting outlay population script..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OutlayRT.settings')
	from repo.models import Repo, Expenses
	populate()
