#     font-family: Georgia,serif;


from django.db import models
# Create your models here.
from autoslug import AutoSlugField
from django.template.defaultfilters import slugify

import appCodeCollections.collections._default as DEFAULTs
# from .models import *



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
	extension = models.CharField(max_length=10, default=None, null=True);
	slug = AutoSlugField(populate_from='name');
	# this function save name's slug automatically...
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
	def __str__(self):
		return "Added a new Programming Language : "+self.name+".";

class DSAsSheetsLists(models.Model):
	name = models.CharField(max_length=100);
	slug = AutoSlugField(populate_from='name');
	by = models.CharField(max_length=100, default=None, null=True);
	reference = models.CharField(max_length=200, default=None, null=True);
	# this function save name's slug automatically...
	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super().save(*args, **kwargs)
	def __str__(self):
		return "Added a new DSAsSheetsLists : "+self.name+".";





class Problems(models.Model):
	title = models.CharField(max_length=100);
	filename = models.CharField(max_length=150, default=None, null=True); 
	slug = AutoSlugField(populate_from='title');
	plateforms = models.IntegerField(default=0, null=True);
	links = models.IntegerField(default=0, null=True);
	datastructures = models.IntegerField(default=0, null=True);
	dsasheetlist = models.IntegerField(default=0, null=True);
	subproblem = models.IntegerField(default=0, null=True);
	# detailsset = models.IntegerField(default=0, null=True);
	detailsset = models.CharField(max_length=500, default=None, null=True); 
	timecomplexity = models.CharField(max_length=35, default=None, null=True);
	auxiliaryspace = models.CharField(max_length=35, default=None, null=True);
	SolutionsCount = models.IntegerField(default=0, null=True);   # It indicates, this problem's how much solutions are here right now???
	SolutionsContinueCount = models.IntegerField(default=0, null=True);  # It indicates, this problem's how much solution's we push till now, deleted+existing.
	JoiningDate = models.DateTimeField(auto_now_add=True);
	UpdationDate = models.DateTimeField(auto_now=True); 

	# this function save title's slug automatically...
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)
	def __str__(self):
		return str(self.id)+". "+self.title


class problems_plateforms(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	plateform_id = models.IntegerField(default=None, null=True);

class problems_datastructures(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	datastructure_id = models.IntegerField(default=None, null=True);

class problems_dsasheetlist(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	dsasheetlist_id = models.IntegerField(default=None, null=True);

class problems_links(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE) 
	plateform_id = models.ForeignKey(Plateforms, null=True, on_delete=models.CASCADE) 
	link = models.CharField(max_length=120, default=None, null=True); 
	text = models.CharField(max_length=25, default=None, null=True); 
	def __str__(self):
		return "Problem '"+self.problem_id.title+"'s link '"+self.link+"' is added.";

class SubProblems(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE)
	title = models.CharField(max_length=100);
	slug = AutoSlugField(populate_from='title');

	# this function save title's slug automatically...
	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		super().save(*args, **kwargs)
	def __str__(self):
		return "Problem '"+self.problem_id.title+"'s sub problem '"+self.title+"' is added.";







class Solutions(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE) 
	filename = models.CharField(max_length=150, default=None, null=True); 
	plateforms = models.IntegerField(default=0, null=True);  
	programminglanguages = models.IntegerField(default=0, null=True);	
	datastructures = models.IntegerField(default=0, null=True); 
	attachments = models.IntegerField(default=0, null=True); 
	codesubmissions =models.CharField(max_length=1000, default=None, null=True); 
	timecomplexity = models.CharField(max_length=35, default=None, null=True); 
	auxiliaryspace = models.CharField(max_length=35, default=None, null=True); 
	explainlevel = models.IntegerField(default=1, null=True); 
	JoiningDate = models.DateTimeField(auto_now_add=True); 
	UpdationDate = models.DateTimeField(auto_now=True); 
	def __str__(self):
		return str(self.problem_id.id)+"-"+str(self.id)+". "+ProgrammingLanguages.objects.get(id=self.programminglanguages).name


class solutions_datastructures(models.Model):
	solution_id = models.ForeignKey(Solutions, null=True, on_delete=models.CASCADE)
	datastructure_id = models.IntegerField(default=None, null=True);

class SolutionsAttachments(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE) 
	showntitle = models.CharField(max_length=200, default=None, null=True); 
	link = models.CharField(max_length=200, default=None, null=True); 
	note = models.CharField(max_length=1000, default=None, null=True); 
	def __str__(self):
		title = self.problem_id.title if(self.problem_id) else None
		return f"New Solution's Attachments is added for problem '{title}' with '{self.showntitle}' shown-title. ({self.id})"
		# return str(self.solution_id.problem_id.id)+"-"+str(self.solution_id.id)+". "+ProgrammingLanguages.objects.get(id=self.solution_id.programminglanguages).name+"'s Attachments added."

class SolutionAndSolutionsAttachments(models.Model):
	problem_id = models.ForeignKey(Problems, null=True, on_delete=models.CASCADE) 
	solution_id = models.ForeignKey(Solutions, null=True, on_delete=models.CASCADE) 
	solutionattachments_id = models.ForeignKey(SolutionsAttachments, null=True, on_delete=models.CASCADE) 













