from django.db import models
from driver.models import *
class Ride(models.model):
	RequestID = models.AutoField(primary_key=True)
	CustomerID = models.IntegerField()
	RequestTime = models.DateTimeField(auto_now_add=True)
	AcceptTime = models.DateTimeField()
	isWaiting = models.BooleanField()
	DriverId = models.ForeignKey(Driver)
