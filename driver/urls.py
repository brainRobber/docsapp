from django.conf.urls import url
#from . import views
print "reachers driver urls.py file"
#import views

urlpatterns = [
	#url(r'^add-ride/', 'customer.views.RequestRide', name='RequestRide'),
	url(r'^(?P<driver_id>\d+)/(?P<req_id>\d+)/$', 'driver.views.accept_request', name='accept_request'),
	url(r'^(?P<driver_id>\d+)/$', 'driver.views.DriverStatus', name='driverrides'),
	url(r'^$', 'driver.views.index', name='index')

]
