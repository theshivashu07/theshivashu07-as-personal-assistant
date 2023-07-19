
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











class Problems(models.Model):
	title = models.CharField(max_length=100);
	slug = AutoSlugField(populate_from='title');
	plateforms = models.IntegerField(default=0, null=True);
	datastructures = models.IntegerField(default=0, null=True);
	# detailsset = models.IntegerField(default=0, null=True);												#current_hidden_data 
	detailsset = models.CharField(max_length=500, default=None, null=True);				#current_show_data 
	timecomplexity = models.CharField(max_length=35, default=None, null=True);
	auxiliaryspace = models.CharField(max_length=35, default=None, null=True);
	JoiningDate = models.DateTimeField(auto_now_add=True);
	UpdationDate = models.DateTimeField(auto_now=True);
	# this function save title's slug automatically...
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)

class problems_plateforms(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	plateform_id = models.IntegerField(default=None, null=True);

class problems_datastructures(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	datastructure_id = models.IntegerField(default=None, null=True);

# class problems_detailssets(models.Model):																						#current_hidden_data 
	# problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)			#current_hidden_data 





class Solutions(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE) 
	plateforms = models.IntegerField(default=0, null=True);  
	programminglanguages = models.IntegerField(default=0, null=True);	
	datastructures = models.IntegerField(default=0, null=True); 
	codesubmissions =models.CharField(max_length=1000, default=None, null=True); 
	timecomplexity = models.CharField(max_length=35, default=None, null=True); 
	auxiliaryspace = models.CharField(max_length=35, default=None, null=True); 
	explainlevel = models.IntegerField(default=1, null=True); 
	JoiningDate = models.DateTimeField(auto_now_add=True); 
	UpdationDate = models.DateTimeField(auto_now=True); 

class solutions_datastructures(models.Model):
	solution_id = models.ForeignKey(Solutions, null=True, on_delete=models.CASCADE)
	datastructure_id = models.IntegerField(default=None, null=True);


