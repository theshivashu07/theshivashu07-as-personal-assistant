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
		# termination-conditions
		if(len(Problems.objects.filter(title=request.POST["ProblemsTitle"]))):
			messages.error(request, "Actually, same name's problem already exist in the database!!!")
			# return redirect("/codecollections/add-problem/")
			return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-add.html", thisisReturningDatabase);

		if( request.POST["ProblemsTitle"] != "" and request.POST["ProblemsDetailSet"] != "" ):
			object = BulkViewFunctions.AddProblems(request)																#wantchange___
			messages.success(request, "New problem '" + object.title +"' is added.")
			return redirect("/codecollections/problem/"+object.slug+"/")
		messages.error(request, "Problems 'Title' and 'Statement' is must to add!!!  Return-Back and Re-Submit!!!")
		############################################
		# return
		return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-add.html", BulkViewFunctions.getNewProblemInternalDetails(request));
	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def addSolution(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] ):
			objectSolution = BulkViewFunctions.AddSolutions(request,objectProblem)
			messages.success(request, "Problem '" + objectProblem.title +"' solution is added.")
			return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")
		# print("This is not correct Input's... Reput again!!!")
		messages.error(request, "Solutions 'Code' is must to add!!!")
		############################################
		# return ? 

	thisisReturningDatabase = {
		'ProblemsSlug':objectProblem.slug,   #problemslug
		'ProblemDataSet':BulkViewFunctions.ProblemDataSet(objectProblem),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");






def addProblemAndSolution(request):
	if request.method=="POST":
		# termination-conditions
		if(len(Problems.objects.filter(title=request.POST["ProblemsTitle"]))):
			messages.error(request, "Actually, same name's problem already exist in the database!!!")
			# return redirect(request, request.path, request.POST) 
			# return redirect("/codecollections/add-problem-solution/")
			############################################
			# return ?

		if( request.POST["ProblemsTitle"] != "" and request.POST["ProblemsDetailSet"] != "" ): 
			objectProblem = BulkViewFunctions.AddProblems(request) 
			if( request.POST["SolutionsCodeSubmissions"] ): 
				objectSolution = BulkViewFunctions.AddSolutions(request,objectProblem) 
				# if problem DONE and solution also DONE 
				messages.success(request, "Problem '" + objectProblem.title +"' solution is added.")
				return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")
			# if problem DONE but solution NOT
			messages.success(request, "New problem '" + objectProblem.title +"' is added.")	
			return redirect("/codecollections/problem/"+objectProblem.slug+"/")
		# if problem and solution - both false
		messages.error(request, "Problems 'Title' and 'Statement' is must to add!!!")
		############################################
		# return ?

	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
	}
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

	thisisReturningDatabase = {
		'ProblemsSlug':problemslug,
		'ProblemDataSet':BulkViewFunctions.ProblemDataSet(objectProblem),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
	}
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

	thisisReturningDatabase = {
		'ProblemsSlug':problemslug,
		'ProblemDataSet':BulkViewFunctions.ProblemDataSet(objectProblem),
		'SolutionDataSet':BulkViewFunctions.SolutionDataSet(objectProblem,objectSolution.id),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
	}
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
	# objectSolution=Solutions.objects.get(id=solutionid)
	thisisReturningDatabase = {
		'ProblemDataSet':BulkViewFunctions.ProblemDataSet(objectProblem),	
		'SolutionDataSet':BulkViewFunctions.SolutionDataSet(objectProblem,solutionid),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-show.html", thisisReturningDatabase);



def openProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	thisisReturningDatabase = {
		'ProblemsSlug':problemslug,
		'ProblemDataSet':BulkViewFunctions.ProblemDataSet(objectProblem),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-show.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def problemsWholeList(request):
	thisisReturningDatabase = {
		'AllSolutions':BulkViewFunctions.WholeDataSet(),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/wholelist.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");




def problemsOnly(request):
	thisisReturningDatabase = {
		'AllProblems':BulkViewFunctions.OnlyProblems(),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/onlyproblems.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def openTestingPage(request):
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/testingpage.html");
	# return render(request,"appCodeCollections/404.html");



 













