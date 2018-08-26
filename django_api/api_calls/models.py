from django.db import models
from djongo import models



# Create your models here.

class service_provider(models.Model):
    user_name = models.TextField()
    sa_name = models.TextField()
    cost = models.FloatField()
    lat = models.FloatField()
    long = models.FloatField()
    
    
class Add_api(models.Model):
	title = models.CharField(max_length=200)
	body = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
def __str__(self):
		return '%s %s' % (self.title, self.body)	
	

class Provider(models.Model):
	name=models.TextField()

	Email=models.TextField()

	phone_number=models.TextField()

	Language=models.TextField()

	Currency=models.TextField()
def __str__(self):
		return '%s %s' % (self.name, self.Email)	

class service_area(models.Model):
    def get_service_area():
        return {"mesaage":"custom"}

	# name=models.TextField()

	# lat=models.FloatField()
	# lng=models.FloatField()


def __str__(self):
		return self.user_name