from django.db import models

class Record(models.Model):
	date = models.DateField()
	eventname = models.CharField(max_length=200, blank=True, null=True)
	adobe =  models.CharField(max_length=200, blank=True, null=True)
	record =  models.TextField( blank=True, null=True)
	hero =  models.CharField(max_length=200, blank=True, null=True)
	source =  models.CharField(max_length=250, blank=True, null=True)
	note = models.TextField( blank=True, null=True)
	export_pdf = models.BooleanField(default=False)
	fileupload = models.CharField( max_length= 300, blank=True, null=True)
 
	def __str__(self):
		return self.eventname
