from django.db import models

class Driver(models.Model):
	driverId = models.AutoField(primary_key=True)
	first_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)

# Create your models here.
