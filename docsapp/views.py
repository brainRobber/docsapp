import json, os, time, shutil, logging
from django.shortcuts import render, render_to_response
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.db import transaction, IntegrityError

from docsapp.models import Ride

import datetime
from django.utils import timezone

def Dashboard(request):
	rides = Ride.objects.all()
	resp_dic = []
	for ride in rides:
		dic = {
				'request_id': ride.RequestID,
				'customer_id': ride.CustomerID,
				'driver_id': ride.DriverID,
				'time_elapsed': int((timezone.now() - ride.RequestTime).total_seconds()/60) 
			}
		if ride.DriverID == 0:
			dic['status'] = 'waiting'
		elif ride.AcceptTime and ride.isCompleted == 0 and int((timezone.now() - ride.AcceptTime).total_seconds()/60) < 5:
			dic['status'] = 'ongoing'
		else:
			dic['status'] = 'completed'
			ride.isCompleted = 1
			ride.save()
		resp_dic.append(dic)

	return render_to_response('dashboard.html', context={'rides' : resp_dic}, content_type=None)
