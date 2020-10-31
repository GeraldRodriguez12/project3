from django.db import models


# Create your models here.

class LIST(models.Model):
	title = models.CharField(max_length=30)


	def __str__(self):
		return self.title

class INFO(models.Model):
	fullname = models.CharField(max_length=100)
	telephone = models.CharField(max_length=100)
	age = models.CharField(max_length=2)
	description = models.ForeignKey(LIST, on_delete=models.CASCADE)



