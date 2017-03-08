import json, os, time, shutil, logging
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.db import transaction, IntegrityError

from docsapp.models import Ride

import datetime
from django.utils import timezone

def index(request):
	context = {}
	return render(request, 'driver/driver.html', context)


@csrf_exempt
def DriverStatus(request, driver_id):
	print "reached driverstatus view"
	resp = {}
	print driver_id
	# waiting requests
	resp_waiting = []
	p = Ride.objects.filter(DriverID=0)
	print p
	print p.count()
	for obj in p:
		dic = {	'request_id': obj.RequestID,
				'customer_id': obj.CustomerID,
				#'request_time': obj.RequestTime,
				'time_elapsed': int((timezone.now() - obj.RequestTime).total_seconds()/60)
			} 
		print dic
		resp_waiting.append(dic)
	
	resp['waiting_list'] = resp_waiting
	#print resp['waiting_list']
	


	#ongoing requests
	objects = Ride.objects.filter(DriverID=driver_id, isCompleted=0)
	print objects.count()
	resp_ongoing = []
	for obj in objects:
		dic = { 
				'request_id': obj.RequestID,
				'customer_id': obj.CustomerID,
				'request_time_elapsed': int((timezone.now() - obj.RequestTime).total_seconds()/60),
				'ongoing_time_elapsed': int((timezone.now() - obj.AcceptTime).total_seconds()/60)
		}
		if dic['ongoing_time_elapsed'] >= 5:
			obj.isCompleted = 1
			obj.save()
		else:
			resp_ongoing.append(dic)
	resp['ongoing_list'] = resp_ongoing
	#print resp['ongoing_list']
	
	
	#completed
	resp_completed = []
	objects = Ride.objects.filter(DriverID=driver_id, isCompleted=1)
	for obj in objects:
		dic = {	'request_id': obj.RequestID,
				'customer_id': obj.CustomerID,
				'request_time_elapsed': int((timezone.now() - obj.RequestTime).total_seconds()/60),
				'pickedup_time_elapsed': int((timezone.now() - obj.AcceptTime).total_seconds()/60),
				'completed_time_elapsed': int((timezone.now() - obj.AcceptTime).total_seconds()/60) - 5

			}
		resp_completed.append(dic)
	resp['completed_list'] = resp_completed
	

	resp['status'] = 'success'
	resp['title'] = 'hello boy'

	return render_to_response('driver/driverlist.html', context={'driver_id': driver_id, 'waiting_list': resp_waiting, 'ongoing_list': resp_ongoing, 'completed_list': resp_completed}, content_type=None)

def accept_request(request, driver_id, req_id):
	resp = {}
	error = {}
	ride_obj = Ride.objects.get(RequestID=req_id)
	
	if ride_obj.DriverID == 0:
		ride_obj.DriverID = driver_id
		ride_obj.AcceptTime = timezone.now()
		ride_obj.save()
	else:
		error_msg = 'Sorry, this ride has been picked by some other driver.'

	resp['status'] = 'success'
	return HttpResponse(json.dumps(resp), content_type='application/json')
# Create your views here.
