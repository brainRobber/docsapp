from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	print "customer view"
	context = {}
	return render(request, 'customer/customer.html', context)


def addRide(request):
	print "inside add ride"
	customer_id = request.data['customer_id']

	p = Ride.objects.get(customerID='customer')
	if not p:
		new_ride = Ride(customerID=customer_id, iswaiting=True)
		new_ride.save()