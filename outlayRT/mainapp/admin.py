from django.contrib import admin
from mainapp.models import Expenses, Repo, UserProfile
from django.contrib.sessions.models import Session

admin.site.register(Expenses)
admin.site.register(Repo)
admin.site.register(UserProfile)
admin.site.register(Session)