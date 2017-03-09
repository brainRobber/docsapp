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
	
	customer_id = request.POST['customerid']  
	ride = Ride.objects.filter(CustomerID=customer_id, isCompleted=0)
	if ride:
		resp['status'] = 'error'
		resp['error'] = 'Previous request already pending'
		return HttpResponse(json.dumps(resp), content_type='application/json')

	try:
		new_ride = Ride(CustomerID=customer_id, isCompleted=0, DriverID=0)
		new_ride.save()
	except Exception, e:
		print 'error occured %s'%e
		error = True
	if error == False:
		resp['status'] = 'success'
	else:
		resp['status'] = 'error'
		resp['error'] = 'Some random error occured'

	return HttpResponse(json.dumps(resp), content_type='application/json')