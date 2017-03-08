from django.shortcuts import render
import datetime

def DriverStatus(request):
	driver_id = request.data['driver_id']
	resp = {}
	# waiting requests
	resp_waiting = []
	p = Ride.objects.filter(DriverId=1)
	for obj in p:
		dic = {'request_id': obj.RequestID,
			'customer_id': obj.CustomerID,
			'request_time': obj.RequestTime,
			'time_elapsed'; (datetime.datetime() - obj.RequestTime).total_seconds()/60
			} 
		resp_waiting.append(dic)
	#ongoing requests
	objects = Ride.Objects.filter(DriverID=driver_id, isCompleted=0)
	for obj in objects:
		dic = { 'request_id': obj.RequestID,
			'customer_id': obj.CustomerID,
			'request_time_elapsed': (datetime.datetime() - obj.RequestTime).total_seconds()/60,
			'ongoing_time_elapsed': (datetime.datetime() - obj.AcceptedTime).total_seconds()/60
		}
		resp_ongoing.append(dic)
	resp_completed = []
	objects = Ride.objects.filter(DriverID=driver_id, isCompleted=1)
	for obj in objects:
		dic = {	'request_id': obj.RequestID,
			'customer_id': obj.CustomerID,
			'request_time_elapsed': (datetime.datetime() - obj.RequestTime).total_seconds()/60,
			'pickedup_time_elapsed': (date
		

def SelectRide(request):
	resp = {}
	request_id = request.data['request_id']
	ride_obj = Ride.Objects.get(RequestID=request_id)
	if not ride_obj:
		print "error message"
	if ride_obj.DriverID == 0:
		ride_obj.DriverID = driver_id
		ride_obj.AcceptedTime = datetime.datetime()
		ride_obj.save()
	else:
		error_msg = 'Sorry, this ride has been picked by some other driver.'
	resp['status'] = 'success'
	return HttpResponse(json.dumps(resp), content_type='application/json')
# Create your views here.
