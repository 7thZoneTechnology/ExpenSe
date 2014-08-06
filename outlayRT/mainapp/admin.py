from django.contrib import admin
from mainapp.models import Expenses, UserProfile, Macros
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User

admin.site.register(Expenses)
admin.site.register(Macros)
admin.site.register(UserProfile)
admin.site.register(Session)