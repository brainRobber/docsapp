from django.db import models
from driver.models import *

class Ride(models.Model):
	RequestID = models.AutoField(primary_key=True)
	CustomerID = models.IntegerField()
	RequestTime = models.DateTimeField(auto_now_add=True)
	AcceptTime = models.DateTimeField(null=True, blank=True)
	isCompleted = models.BooleanField()
	DriverID = models.IntegerField()
