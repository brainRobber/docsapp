from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	print "docsapp view"
	context = {}
	return render(request, 'index.html', context)
# Create your views here
.