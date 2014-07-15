from django.contrib import admin
from repo.models import Expenses, Repo, UserProfile

admin.site.register(Expenses)
admin.site.register(Repo)
admin.site.register(UserProfile)
