from django.db import models

# Create your models here.
class Project(models.Model):
	title = models.CharField(max_length=40,default='Project')
	image = models.ImageField(upload_to='images/')
	summary = models.CharField(max_length=5000)
	link = models.CharField(max_length=2000,default='#')

	def __str__(self):
		return self.title
