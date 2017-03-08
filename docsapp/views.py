from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	print "docsapp view"
	context = {}
	return render(request, 'index.html', context)
# Create your views here


def Dashboard(request):
	p = Ride.Objects.all()
	resp_dic = {}
	for i in p:
		if Time.now() - 
	resp_dic.append = {
				'request_id': i.RequestId,
				'customer_id': i.customerID,
				'time elapsed': 
				'Status': i.
	}
