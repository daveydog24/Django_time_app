from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
	context = {
		'Date': strftime("%b %d, %Y"),
		'Time': strftime("%H:%M %p")
	}
	return render(request, 'time_display/index.html', context)