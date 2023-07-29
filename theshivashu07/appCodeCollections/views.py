from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

from .models import *
import appCodeCollections.collections.BulkViewFunctions as BulkViewFunctions
from django.contrib import messages



# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


def index(request):
	messages.success(request, "Welcome to theCodeCollections's HOME Page!!!")
	return render(request,"appCodeCollections/index.html");

def edittables(request):
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		comingData=request.POST["comingData"]
		if(comingFrom in ['Plateform', 'DataStructure', 'ProgrammingLanguage']):
			lock= ( Plateforms() if(comingFrom=='Plateform') else ( DataStructures() if(comingFrom=='DataStructure') else ProgrammingLanguages() ) )
			lock.name=comingData;
			lock.save()
			messages.success(request, comingData+" added on '"+comingFrom + "' Database.")
		return redirect("/codecollections/edit-tables/")

	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
	}
	return render(request,"appCodeCollections/edittables.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");







def addProblem(request): 
	# problemID=Problems.objects.get(slug=defaultSlug)
	if request.method=="POST":

		# termination-conditions  -  if problem already exist, then we move this to the oroginal problem side...
		objectProblemLists = Problems.objects.filter(title=request.POST["ProblemsTitle"])
		if(bool(objectProblemLists)):
			# we know that their is only one problem exist with same name, thats-it...
			objectProblem = objectProblemLists[0] 
			messages.error(request, "Actually, same name's problem already exist in the database!!! See this opened problem...")
			return redirect("/codecollections/problem/"+objectProblem.slug+"/")

		# what if you put blank your problem's "title" or "detailsset", then we sent back to the same place again...
		# we'll I'm already managing this, with set 'required' in these field, but always play safe, may I'll be forgrt... 
		if( request.POST["ProblemsTitle"] == "" or request.POST["ProblemsDetailSet"] == "" ):
			messages.error(request, "Problems 'Title' and 'Statement' is must to add!!!  Return-Back and Re-Submit!!!")
			thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
			thisisReturningDatabase.update( BulkViewFunctions.getbackProblemDetails(request) )
			return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-add.html", thisisReturningDatabase);

		# now this place is the safest place, so now add problem...
		object = BulkViewFunctions.AddProblems(request)
		messages.success(request, "New problem '" + object.title +"' is added.")
		return redirect("/codecollections/problem/"+object.slug+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def addSolution(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] == "" ):
			messages.error(request, "Solution's 'code' is must to add!!!")
			thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
			thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
			thisisReturningDatabase.update( BulkViewFunctions.getbackSolutionDetails(request) )
			return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);

		# now this place is the safest place, so now add solution...
		objectSolution = BulkViewFunctions.AddSolutions(request,objectProblem)
		messages.success(request, "Problem '" + objectProblem.title +"' solution is added.")
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");






def addProblemAndSolution(request):
	if request.method=="POST":		
		# termination-conditions  -  if problem already exist, then we move this to the oroginal problem side...
		objectProblemLists = Problems.objects.filter(title=request.POST["ProblemsTitle"])
		if(bool(objectProblemLists)):
			# we know that their is only one problem exist with same name, thats-it...
			objectProblem = objectProblemLists[0] 
			messages.error(request, "Actually, same name's problem already exist in the database!!! See this opened problem...")
			return redirect("/codecollections/problem/"+objectProblem.slug+"/")

		# what if you put blank your problem's "title" or "detailsset", then we sent back to the same place again...
		# we'll I'm already managing this, with set 'required' in these field, but always play safe, may I'll be forgrt... 
		if( request.POST["ProblemsTitle"] == "" or request.POST["ProblemsDetailSet"] == "" ):
			messages.error(request, "Problems 'Title' and 'Statement' is must to add!!!  Please Re-Submit again!!!")
			thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
			thisisReturningDatabase.update( BulkViewFunctions.getbackProblemDetails(request) )
			thisisReturningDatabase.update( BulkViewFunctions.getbackSolutionDetails(request) )
			return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-add.html", thisisReturningDatabase);

		# now this place is the safest place, so now add problem...
		objectProblem = BulkViewFunctions.AddProblems(request)
		messages.success(request, "New problem '" + objectProblem.title +"' is added.")

		######################################################################################
		# SOLUTION's --------------------------------------------------------------------------------------------------------------------------------------------------
		if( request.POST["SolutionsCodeSubmissions"] == "" ):
			messages.error(request, "Solution's 'code' is must to add!!! Please fill all fields again...")
			thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
			return redirect("/codecollections/add-solution/"+objectProblem.slug+"/")
			# return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);

		# now this place is the safest place, so now add solution...
		objectSolution = BulkViewFunctions.AddSolutions(request,objectProblem)
		messages.success(request, "Problem '" + objectProblem.title +"' solution is added.")
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");



def editProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	if request.method=="POST":
		if( request.POST["ProblemsTitle"] and request.POST["ProblemsDetailSet"] ):
			BulkViewFunctions.EditProblems(request,objectProblem)																			#wantchange___
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problem/"+objectProblem.slug+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-edit.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");

def editSolution(request, problemslug, solutionid):
	objectProblem=Problems.objects.get(slug=problemslug)
	objectSolution=Solutions.objects.get(id=solutionid)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] ):
			BulkViewFunctions.EditSolutions(request,objectProblem,objectSolution.id)
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	thisisReturningDatabase['SolutionDataSet'] = BulkViewFunctions.SolutionDataSet(objectProblem,objectSolution.id)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-edit.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");




def deleteProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	objectProblem.delete()
	return redirect("/codecollections/problems-with-solutions/")

def deleteSolution(request, problemslug, solutionid):
	objectSolution=Solutions.objects.get(id=solutionid)
	objectSolution.delete()
	return redirect("/codecollections/problems-with-solutions/")







def ProblemWithSolution(request, problemslug, solutionid):
	objectProblem=Problems.objects.get(slug=problemslug)

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	thisisReturningDatabase['SolutionDataSet'] = BulkViewFunctions.SolutionDataSet(objectProblem,solutionid)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-show.html", thisisReturningDatabase);



def openProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['ProblemDataSet'] = BulkViewFunctions.ProblemDataSet(objectProblem)
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-show.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def problemsWholeList(request):

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['AllSolutions'] = BulkViewFunctions.WholeDataSet()
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/wholelist.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");




def problemsOnly(request):

	thisisReturningDatabase = BulkViewFunctions.getBaseStructure()
	thisisReturningDatabase['AllProblems'] = BulkViewFunctions.OnlyProblems()
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/onlyproblems.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def openTestingPage(request):
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/testingpage.html");
	# return render(request,"appCodeCollections/404.html");



 













