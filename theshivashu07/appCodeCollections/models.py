
from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify


class DataStructures(models.Model):
	name = models.CharField(max_length=25);
	slug = AutoSlugField(populate_from='name');
	# this function save name's slug automatically...
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
	def __str__(self):
		return "Added a new Data Structure : "+self.name+".";

class Plateforms(models.Model):
	name = models.CharField(max_length=25);
	slug = AutoSlugField(populate_from='name');
	color = models.CharField(max_length=25, default=None, null=True);
	bgcolor = models.CharField(max_length=25, default=None, null=True);	
	# this function save name's slug automatically...
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
	def __str__(self):
		return "Added a new Plateform : "+self.name+".";

class ProgrammingLanguages(models.Model):
	name = models.CharField(max_length=25);
	slug = AutoSlugField(populate_from='name');
	# this function save name's slug automatically...
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
	def __str__(self):
		return "Added a new Programming Language : "+self.name+".";



