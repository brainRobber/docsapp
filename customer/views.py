from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	print "customer view"
	context = {}
	return render(request, 'customer/customer.html', context)


def addRide(request):
	print "inside add ride"