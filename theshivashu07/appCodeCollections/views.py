from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.

import appCodeCollections._BulkFunctions as _BulkFunctions
from .models import *




# def index(request):
	# return HttpResponse("Hey <b>Shivam Shukla</b>, <b style='font-size:10px'>N your url '@theshivashu07'</b> !!!");


def index(request):
	return render(request,"appCodeCollections/index.html");

def edittables(request):
	if request.method=="POST":
		comingFrom=request.POST["comingFrom"]
		comingData=request.POST["comingData"]
		if(comingFrom=='Plateform'):
			lock=Plateforms()
			lock.name=comingData;
			lock.save()
		elif(comingFrom=='DataStructure'):
			lock=DataStructures()
			lock.name=comingData;
			lock.save()
		elif(comingFrom=='ProgrammingLanguage'):
			lock=ProgrammingLanguages()
			lock.name=comingData;
			lock.save()
		else:
			print("Go to somewhere else.....")
		return redirect("/codecollections/edittables/")
	thisisReturningDatabase = {
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'DataStructures' : DataStructures.objects.all(), 
		'Plateforms' : Plateforms.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/edittables.html", thisisReturningDatabase);

def codesubmissions(request):
	return render(request,"appCodeCollections/404.html");

def problemsubmissions(request):
	return render(request,"appCodeCollections/404.html");












def addProblem(request): 
	# problemID=Problems.objects.get(slug=defaultSlug)
	if request.method=="POST":
		if( request.POST["ProblemsTitle"] and request.POST["ProblemsDetailSet"] ):
			object = _BulkFunctions.AddProblems(request)																#wantchange___
			# _BulkFunctions.EditProblems(request,problemID)														#wantchange___
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/solution/"+object.slug+"/")
	
	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");

def addSolution(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] ):
			objectSolution = _BulkFunctions.AddSolutions(request,objectProblem)
			# _BulkFunctions.EditSolutions(request,objectProblem)
		else:
			print("This is not correct Input's... Reput again!!!")
		# print(objectProblem.slug, type(objectProblem.slug), objectSolution.id, type(objectSolution.id))
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = {
		'ProblemsSlug':objectProblem.slug,   #problemslug
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(objectProblem),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");






def addProblemAndSolution(request):
	if request.method=="POST":
		if( request.POST["ProblemsTitle"] and request.POST["ProblemsDetailSet"] ):
			objectProblem = _BulkFunctions.AddProblems(request)																					#wantchange___
			if( request.POST["SolutionsCodeSubmissions"] ):
				objectSolution = _BulkFunctions.AddSolutions(request,objectProblem)
			else:
				print("We're Discard only Solution... Reput again!!!")
		else:
			print("We're Discard both Problem and Solution... Reput again!!!")
		print("__________________________________________________________________")
		print("______________________________DONE______________________________")
		print("__________________________________________________________________")
		print(f"  /codecollections/problem-solution/{objectProblem.slug}/{objectSolution.id}/  ")
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = {
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-add.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");



def editProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	if request.method=="POST":
		if( request.POST["ProblemsTitle"] and request.POST["ProblemsDetailSet"] ):
			_BulkFunctions.EditProblems(request,objectProblem)																			#wantchange___
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problem/"+objectProblem.slug+"/")

	thisisReturningDatabase = {
		'ProblemsSlug':problemslug,
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(objectProblem),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-edit.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");

def editSolution(request, problemslug, solutionid):
	objectProblem=Problems.objects.get(slug=problemslug)
	objectSolution=Solutions.objects.get(id=solutionid)
	if request.method=="POST":
		if( request.POST["SolutionsCodeSubmissions"] ):
			_BulkFunctions.EditSolutions(request,objectProblem,objectSolution.id)
		else:
			print("This is not correct Input's... Reput again!!!")
		return redirect("/codecollections/problem-solution/"+objectProblem.slug+"/"+str(objectSolution.id)+"/")

	thisisReturningDatabase = {
		'ProblemsSlug':problemslug,
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(objectProblem),
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(objectProblem,objectSolution),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/solution-edit.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");





def problemsWholeList(request):
	thisisReturningDatabase = {
		'AllSolutions':_BulkFunctions.SolutionDataSet(objectProblem,objectSolution),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/wholelist.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");




def ProblemWithSolution(request, problemslug, solutionid):
	print(problemslug, solutionid)
	objectProblem=Problems.objects.get(slug=problemslug)
	# objectSolution=Solutions.objects.get(id=solutionid)
	thisisReturningDatabase = {
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(objectProblem),	
		'SolutionDataSet':_BulkFunctions.SolutionDataSet(objectProblem,solutionid),
		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-solution-show.html", thisisReturningDatabase);



def openProblem(request, problemslug):
	objectProblem=Problems.objects.get(slug=problemslug)
	thisisReturningDatabase = {
		'ProblemsSlug':problemslug,
		'ProblemDataSet':_BulkFunctions.ProblemDataSet(objectProblem),

		'Plateforms' : Plateforms.objects.all(),
		'DataStructures' : DataStructures.objects.all(),
		'ProgrammingLanguages' : ProgrammingLanguages.objects.all(),
		'problemslug' : 'problem-number-0001',
		'solutionid' : 1,
	}
	return render(request,"appCodeCollections/Problems-Solutions-Mini-Templates/problem-show.html", thisisReturningDatabase);
	# return render(request,"appCodeCollections/404.html");











 



'''

BULK - DATA - ASSIGNMENT

	if request.method=="POST":
		for key in _importantdatasets.Plateforms:
			locks=Plateforms()
			locks.name=key
			locks.save()
		count=0
		for key in _importantdatasets.DataStructures:
			count+=1
			if(count==15):
				break;
			locks=DataStructures()
			locks.name=key
			locks.save()
		for key in _importantdatasets.ProgrammingLanguages:
			locks=ProgrammingLanguages()
			locks.name=key
			locks.save()
		return redirect("/codecollections/edittables/")
'''















