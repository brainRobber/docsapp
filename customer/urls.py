from django.conf.urls import url
#from . import views
print "reachers customer urls.py file"
#import views

urlpatterns = [
	url(r'^add-ride/', 'customer.views.addRide', name='addRide'),
	url(r'^$', 'customer.views.index', name='index'),
]
