import json, os, time, shutil, logging
from django.shortcuts import render
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.db import transaction, IntegrityError

from docsapp.models import Ride

def index(request):
	print "customer view"
	context = {}
	return render(request, 'customer/customer.html', context)

@csrf_exempt
def RequestRide(request):
	resp = {}
	error = False
	print "inside add ride"
	print request.POST
	print "after this"
	print request.POST['customerid']
	print 'hello'
	customer_id = request.POST['customerid']  
	print customer_id
	#p = Ride.objects.get(customerID='customer')
	try:
		new_ride = Ride(CustomerID=customer_id, isCompleted=0, DriverID=0)
		new_ride.save()
		print "got in db"
	except Exception, e:
		print 'error occured %s'%e
		error = True
		print "yaha nhi aya"
	#else:
	#print "You have already booked a ride and ur request is under process"
	if error == False:
		resp['status'] = 'success'
	else:
		resp['status'] = 'Error'
	print resp
	
	return HttpResponse(json.dumps(resp), content_type='application/json')