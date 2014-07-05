from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from rango.models import User

def index(request):
	context = RequestContext(request)

	

	context_dict = {'boldmessage': "This is bold font from the context"}

	return render_to_response('account/index.html', context_dict, context)

	

